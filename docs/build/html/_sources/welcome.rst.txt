Welcome to BrainStorm!
**********************

Hello these are the base instructions for running my project and quick start.

Getting started
===============
Prequisites:

python 3.8

Git

Virtualenv

Docker

docker-compose

Installation
============

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

Quick start
===========
Simply run:

./run-pipeline.sh - to run all the components.

When you want to upload data run:

Run: python -m Brain_Storm.client upload-sample <mind file>

