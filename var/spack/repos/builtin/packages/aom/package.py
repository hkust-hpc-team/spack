# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Aom(CMakePackage):
    """Alliance for Open Media AOM AV1 Codec Library"""

    homepage = "https://aomedia.googlesource.com/aom"
    git = "https://aomedia.googlesource.com/aom"

    license("BSD-2-Clause AND AOM-Patent-License-1.0", checked_by="tgamblin")

    version("3.12.1", tag="v3.12.1")
    version("3.12.0", tag="v3.12.0")
    version("3.11.0", tag="v3.11.0")
    version("3.10.0", tag="v3.10.0")
    version("3.8.3", tag="v3.8.3")
    version("3.9.1", tag="v3.9.1")
    version("3.9.0", tag="v3.9.0")
    version("3.8.2", tag="v3.8.2")
    version("3.8.1", tag="v3.8.1")
    version("3.7.2", tag="v3.7.2")
    version("3.8.0", tag="v3.8.0")
    version("3.7.1", tag="v3.7.1")
    version("3.7.0", tag="v3.7.0")
    version("3.6.1", tag="v3.6.1")
    version("3.6.0", tag="v3.6.0")
    version("3.5.0", tag="v3.5.0")
    version("3.4.0", tag="v3.4.0")
    version("3.3.0", tag="v3.3.0")
    version("3.2.0", tag="v3.2.0")
    version("3.1.3", tag="v3.1.3")
    version("3.1.2", tag="v3.1.2")
    version("3.1.1", tag="v3.1.1")
    version("3.1.0", tag="v3.1.0")
    version("3.0.0", tag="v3.0.0")
    version("2.0.2", tag="v2.0.2")
    version("2.0.1", tag="v2.0.1")
    version("2.0.0", tag="v2.0.0")
    version(
        "1.0.0-errata1",
        tag="v1.0.0-errata1",
        commit="add4b15580e410c00c927ee366fa65545045a5d9",
    )

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("yasm")

    def cmake_args(self):
        args = []
        args.append("-DBUILD_SHARED_LIBS=ON")
        return args
