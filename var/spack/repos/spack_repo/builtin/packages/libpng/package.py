# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakeBuilder, CMakePackage

from spack.package import *


class Libpng(CMakePackage):
    """libpng is the official PNG reference library."""

    homepage = "http://www.libpng.org/pub/png/libpng.html"
    url = "https://prdownloads.sourceforge.net/libpng/libpng-1.6.37.tar.xz"
    git = "https://github.com/pnggroup/libpng"

    maintainers("AlexanderRichert-NOAA")

    license("Libpng")

    version("1.6.48", sha256="46fd06ff37db1db64c0dc288d78a3f5efd23ad9ac41561193f983e20937ece03")
    version("1.6.47", sha256="b213cb381fbb1175327bd708a77aab708a05adde7b471bc267bd15ac99893631")
    version("1.6.46", sha256="f3aa8b7003998ab92a4e9906c18d19853e999f9d3bca9bd1668f54fa81707cb1")
    version("1.6.45", sha256="926485350139ffb51ef69760db35f78846c805fef3d59bfdcb2fba704663f370")
    version("1.6.44", sha256="60c4da1d5b7f0aa8d158da48e8f8afa9773c1c8baa5d21974df61f1886b8ce8e")
    version("1.6.43", sha256="6a5ca0652392a2d7c9db2ae5b40210843c0bbc081cbd410825ab00cc59f14a6c")
    version("1.6.42", sha256="c919dbc11f4c03b05aba3f8884d8eb7adfe3572ad228af972bb60057bdb48450")
    version("1.6.41", sha256="d6a49a7a4abca7e44f72542030e53319c081fea508daccf4ecc7c6d9958d190f")
    version("1.6.40", sha256="535b479b2467ff231a3ec6d92a525906fb8ef27978be4f66dbe05d3f3a01b3a1")
    version("1.6.39", sha256="1f4696ce70b4ee5f85f1e1623dc1229b210029fa4b7aee573df3e2ba7b036937")
    version("1.6.38", sha256="b3683e8b8111ebf6f1ac004ebb6b0c975cd310ec469d98364388e9cedbfa68be")
    version("1.6.37", sha256="505e70834d35383537b6491e7ae8641f1a4bed1876dbfe361201fc80868d88ca")
    # From http://www.libpng.org/pub/png/libpng.html (2019-04-15)
    #     libpng versions 1.6.36 and earlier have a use-after-free bug in the
    #     simplified libpng API png_image_free(). It has been assigned ID
    #     CVE-2019-7317. The vulnerability is fixed in version 1.6.37,
    #     released on 15 April 2019.

    # Required for qt@3
    version("1.5.30", sha256="7d76275fad2ede4b7d87c5fd46e6f488d2a16b5a69dc968ffa840ab39ba756ed")
    version("1.2.57", sha256="0f4620e11fa283fedafb474427c8e96bf149511a1804bdc47350963ae5cf54d8")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("cmake@3.14:", type="build", when="@1.6.47:")
    depends_on("cmake@3.1:", type="build", when="@1.6.37:")
    depends_on("cmake@2.8.3:", type="build", when="@1.5.30:")
    depends_on("cmake@2.4.3:", type="build", when="@1.2.57:")

    depends_on("zlib-api")

    variant(
        "libs",
        default="shared,static",
        values=("shared", "static"),
        multi=True,
        description="Build shared libs, static libs or both",
    )
    variant("pic", default=False, description="PIC")

    # Tries but fails to include fp.h, removed in libpng 1.6.45
    conflicts("@:1.6.44", when="%apple-clang@17:")

    @property
    def libs(self):
        # v1.2 does not have a version-less symlink
        libraries = f"libpng{self.version.up_to(2).joined}"
        shared = self.spec.satisfies("libs=shared")
        return find_libraries(
            libraries, root=self.prefix, shared=shared, recursive=True, runtime=False
        )


class CMakeBuilder(CMakeBuilder):
    def cmake_args(self):
        args = [
            self.define("CMAKE_CXX_FLAGS", self.spec["zlib-api"].headers.include_flags),
            self.define("ZLIB_ROOT", self.spec["zlib-api"].prefix),
            self.define("PNG_SHARED", "shared" in self.spec.variants["libs"].value),
            self.define("PNG_STATIC", "static" in self.spec.variants["libs"].value),
            self.define_from_variant("CMAKE_POSITION_INDEPENDENT_CODE", "pic"),
        ]
        zlib_lib = self.spec["zlib-api"].libs
        if zlib_lib:
            args.append(self.define("ZLIB_LIBRARY", zlib_lib[0]))
        if self.spec.satisfies("platform=darwin target=aarch64:"):
            args.append("-DPNG_ARM_NEON=off")
        return args
