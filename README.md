# Valar-dagger

[![Version status](https://img.shields.io/pypi/status/valar.dagger?label=status)](https://pypi.org/project/valar.dagger)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python version compatibility](https://img.shields.io/pypi/pyversions/valar.dagger?label=Python)](https://pypi.org/project/valar.dagger)
[![Version on Docker Hub](https://img.shields.io/docker/v/dmyersturnbull/valar-dagger?color=green&label=Docker%20Hub)](https://hub.docker.com/repository/docker/dmyersturnbull/valar-dagger)
[![Version on Github](https://img.shields.io/github/v/release/dmyersturnbull/valar-dagger?include_prereleases&label=GitHub)](https://github.com/dmyersturnbull/valar-dagger/releases)
[![Version on PyPi](https://img.shields.io/pypi/v/valar.dagger?label=PyPi)](https://pypi.org/project/valar.dagger)  
[![Build (Actions)](https://img.shields.io/github/workflow/status/dmyersturnbull/valar-dagger/Build%20&%20test?label=Tests)](https://github.com/dmyersturnbull/valar-dagger/actions)
[![Documentation status](https://readthedocs.org/projects/valar-dagger/badge)](https://valar-dagger.readthedocs.io/en/stable)
[![Coverage (coveralls)](https://coveralls.io/repos/github/dmyersturnbull/valar-dagger/badge.svg?branch=main&service=github)](https://coveralls.io/github/dmyersturnbull/valar-dagger?branch=main)
[![Maintainability (Code Climate)](https://api.codeclimate.com/v1/badges/eea2b741dbbbb74ad18a/maintainability)](https://codeclimate.com/github/dmyersturnbull/valar-dagger/maintainability)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/dmyersturnbull/valar-dagger/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/dmyersturnbull/valar-dagger/?branch=main)

Scheduler for [Valar](https://github.com/dmyersturnbull/valar-schema) backend tasks: run insertion, feature insertion, and backups.

To use:
1. Make sure MariaDB is running.
2. Install [valar-backend](https://github.com/dmyersturnbull/valar-backend).
3. Run `scripts/stage-all` to build and stage JARs to `/var/stage/`.
4. If you haven't already, create a skeleton database using `valarpy create-skeleton`.
5. Install [valarpy](https://github.com/dmyersturnbull/valarpy) and edit the config file.
6. Run `pip install valar-dagger && valar-dagger init`.
7. Edit the newly created `/etc/valar-dagger.toml`
   ([example](https://github.com/dmyersturnbull/valar-dagger/blob/master/valardagger/resources/valar-dagger.toml)).
8. Run `nohup valar-dagger start`.

[New issues](https://github.com/dmyersturnbull/valar-dagger/issues) and pull requests are welcome.
Please refer to the [contributing guide](https://github.com/dmyersturnbull/valar-dagger/blob/master/CONTRIBUTING.md)
and [security policy](https://github.com/dmyersturnbull/valar-dagger/blob/master/SECURITY.md).  
Generated with [Tyrannosaurus](https://github.com/dmyersturnbull/tyrannosaurus).
