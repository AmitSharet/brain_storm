[![Build Status](https://travis-ci.org/AmitSharet/brain_storm.svg?branch=master)](https://travis-ci.org/AmitSharet/brain_storm)
[![codecov](https://codecov.io/gh/AmitSharet/brain_storm/branch/master/graph/badge.svg)](https://codecov.io/gh/AmitSharet/brain_storm)

# Welcome to BrainStorm!

Hello, I'm able to read minds from sample files, upload them to a server, I can have various of parsers to parse the thoughts and publish them later to a nice GUI.

# Getting started

## Prequisites:

* python 3.8
* Git
* Virtualenv
* Docker
* docker-compose 

## Installation

Clone and enter my repository:

    $ git clone https://github.com/AmitSharet/brain_storm.git
    ...
    $ cd brain_storm

Run installation script 

    $ ./scripts/install.sh
    ...
    $ source ./env/bin/activate

 Check everything is working as expected:

    $ pytest tests/
    ...

## Quick start

Simply run:

    `docker-compose up -d

## Full documentation

You can find full documentation of my project here:

https://brain-storm.readthedocs.io/en/latest/