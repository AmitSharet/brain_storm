[![Build Status](https://travis-ci.org/AmitSharet/brain_storm.svg?branch=master)](https://travis-ci.org/AmitSharet/brain_storm)

# Welcome to BrainStorm!

Hello, I'm able to read minds from sample files, upload them to a server, I can have various of parsers to parse the thoughts and publish them later to a nice GUI.

# Getting started

## Prequisites:

* python 3.8
* Git
* Virtualenv
* Docker
* docker-compose 
* npm

## Installation

Clone and enter my repository:

    $ git clone https://github.com/AmitSharet/brain_storm.git
    ...
    $ cd brain_storm

Run installation script 

    $ ./scripts/install.sh
    ...
    $ source .env/bin/activate

 Check everything is working as expected:

    $ pytest tests/
    ...

## Quick start

Simply run:

    ./run-pipeline.sh

(For Dan: honestly I don't recommend using this script for some reasons: 
1. It's not finished yet, I didn't have time left to add the gui to the script
2. sometimes it has problems because of something I haven't figured out yet.
3. I added it because sometimes it works and I preferred adding something in the time I had.
4. I tried working the docker-compose for days, and I guess I didn't manage time dealing with it well enough, that's why I'm using this script.

(this message will be deleted later on))

## Full documentation

You can find full documentation of my project here:

https://brain-storm.readthedocs.io/en/latest/
