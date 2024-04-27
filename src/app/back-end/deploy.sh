#!/bin/bash

# Variables
REMOTE_USER="diego"
REMOTE_HOST="diego.arkania.es"
REPO_URL="git@github.com:TheReported/jhoola.git"
TARGET_DIR="jhoola"

# Conexión SSH y clonar el repositorio
ssh "$REMOTE_USER@$REMOTE_HOST" "
  if [ ! -d $TARGET_DIR ]; then
    echo 'Clonando el repositorio...'
    git clone $REPO_URL
    cd $TARGET_DIR
  else
    echo 'El directorio ya existe.'
    cd $TARGET_DIR
    git pull
  fi
  python3 -m venv .venv --prompt jhoola
  source .venv/bin/activate
  cd src/app/back-end/
  pip install -r requirements.txt
  supervisorctl restart jhoola
"
cd ~/$TARGET_DIR/src/app/back-end/ && scp .env "$REMOTE_USER@$REMOTE_HOST":/home/diego/$TARGET_DIR/
