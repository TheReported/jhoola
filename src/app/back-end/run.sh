#!/bin/bash

cd ~/jhoola/
source .venv/bin/activate
cd src/app/back-end/
gunicorn -b unix:/tmp/jhoola.sock main.wsgi:application
