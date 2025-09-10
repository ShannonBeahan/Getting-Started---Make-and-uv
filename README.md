# Getting-Started---Make-and-uv
Getting started series - how to use make and uv and why

# How to run
make install
make run


# CONTEXT:
What uv.lock is
    When you run uv add requests (or any dependency), uv resolves the exact versions of all packages needed, including transitive dependencies.
    uv saves this information in uv.lock.
    The file ensures that everyone using this project installs the exact same versions of all packages.
    Think of it as locking your dependencies so that your project is reproducible.

How it’s used
    Team reproducibility:
        If you share your project with peers, and they run uv sync, uv will read uv.lock and install the exact versions you used.
    Version consistency:
        Without uv.lock, running uv add requests on two different machines could install slightly different versions of dependencies.
        With uv.lock, the environment is identical everywhere.
    Updating dependencies:
        If you want to upgrade packages, you run uv upgrade <package> or uv sync --upgrade.
        uv will update uv.lock with the new exact versions.