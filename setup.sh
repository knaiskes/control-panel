#!/bin/bash

function dependencyExists() {
    package=$1
    if command -v "$1" >/dev/null; then
        return 0
    else
        return 1
    fi
}

function createVirtualEnviroment {
    if dependencyExists "python"; then
        echo "Creating virtual enviroment";
        python -m venv venv
        echo "Installing dependecies";
        source venv/bin/activate
        pip install -r requirements.txt
    else
        echo "Python is not install on your system";
    fi
}

function migrations {
    echo "Making migrations";
    declare -a migrationsArr=("relays" "dht22")
    echo "${migrationsArr[@]}"
    python controlpanel/manage.py migrate
    python controlpanel/manage.py makemigrations "${migrationsArr[@]}"
}

# Check if venv already exists


createVirtualEnviroment
migrations
