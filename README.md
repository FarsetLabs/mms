Farset Member Management System
===============================

Introduction
------------

Farset's MMS manages users.

Getting Started
---------------

### Running the application

To get started with this application you will require [docker][docker] and
[docker-compose][docker-compose]. If you don't have these tools installed
please see the section of [installing them](#installing-docker).

Once you have these tools installed, it is a as simple as running
`docker-compose up` in the root of the repository to start both the Python
backend and the webpack scripts to build and watch the front-end code. Both
these tasks are run as separate docker containers, orchestrated by
docker-compose.

> #### Running without Docker
>
> The master compose file makes it simple to get up and running, and uses
> docker to keep system-level dependencies to an absolute minimum, but this
> might not cover all the use cases and eventualities of development.
>
> To run the application without docker, enter into the `server` and `ui`
> directories and run `make run` and `make build` (or `make watch`)
> respectively. These commands have their own dependencies (notably nodejs,
> npm, webpack, yarn, and Django) and complications, so please open up the
> makefile and be aware of exactly what commands are being run here.

Appendices
----------

### Installing Docker

**NOTE:** The minimum required version of docker is 1.7.

#### Linux

Docker is best supported on Linux, you can probably find packages for your
preferred distribution [here][docker_install].

#### OSX

We'll assumg a Homebrew and Cask setup, you should run the following:
`brew cask install docker`

#### Windows

Not supported yet (we just haven't tried, give it a go, it might work). Pull
requests very welcome.

[docker]: https://docker.io  "Docker"
[docker_install]: https://docs.docker.com/installation/  "Docker Installation"
[docker-compose]: https://docs.docker.com/compose/
