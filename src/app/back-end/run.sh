#!/bin/bash

cd ~/jhoola/
source .venv/bin/activate
cd src/back-end/
gunicorn -b unix:/tmp/jhoola.sock main.wsgi:application
