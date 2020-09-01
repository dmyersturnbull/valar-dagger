# Valar-dagger

[![Version status](https://img.shields.io/pypi/status/valar-dagger)](https://pypi.org/project/valar-dagger/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/valar-dagger)](https://pypi.org/project/valar-dagger/)
[![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/dmyersturnbull/valar-dagger?include_prereleases&label=GitHub)](https://github.com/dmyersturnbull/valar-dagger/releases)
[![Latest version on PyPi](https://badge.fury.io/py/valar-dagger.svg)](https://pypi.org/project/valar-dagger/)
[![Documentation status](https://readthedocs.org/projects/valar-dagger/badge/?version=latest&style=flat-square)](https://valar-dagger.readthedocs.io/en/stable/)
[![Build & test](https://github.com/dmyersturnbull/valar-dagger/workflows/Build%20&%20test/badge.svg)](https://github.com/dmyersturnbull/valar-dagger/actions)
[![Coverage](https://coveralls.io/repos/github/dmyersturnbull/valar-dagger/badge.svg?branch=master)](https://coveralls.io/github/dmyersturnbull/valar-dagger?branch=master)

Scheduler for Valar backend tasks: run insertion, feature insertion, and backups.

To use:
1. Make sure MariaDB is running.
2. Install [valar-infrastructure](https://github.com/dmyersturnbull/valar-infrastructure).
3. Run `scripts/stage-all` to build and stage JARs to `/var/stage/`.
4. If you haven't already, create a skeleton database using `valarpy create-skeleton`.
5. Install [valarpy](https://github.com/dmyersturnbull/valarpy) and edit the config file.
6. Run `pip install valar-dagger && valar-dagger init`.
7. Edit the newly created `/etc/valar-dagger.toml`
   ([example](https://github.com/dmyersturnbull/valar-dagger/blob/master/valardagger/resources/valar-dagger.toml)).
8. Run `nohup valar-dagger start`.

[New issues](https://github.com/dmyersturnbull/valar-dagger/issues) and pull requests are welcome.
Please refer to the [contributing guide](https://github.com/dmyersturnbull/valar-dagger/blob/master/CONTRIBUTING.md).
Generated with [Tyrannosaurus](https://github.com/dmyersturnbull/tyrannosaurus).
