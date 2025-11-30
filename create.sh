#!/usr/bin/bash

# Used to initialize the repo environment.

python3 -m venv .venv_normal
python -m virtualenv -p pypy3 .venv
