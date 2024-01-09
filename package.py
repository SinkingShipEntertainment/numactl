name = "numactl"

version = "2.0.0.sse.1.0.0"

description = \
    """
    NUMA policy
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]
    #c.build_thread_count = "physical_cores"

requires = [
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"],
]

uuid = "repository.numactl"

# NOTE:
# rez-build -i --build-system cmake
# rez-release --build-system cmake

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
