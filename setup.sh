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

# Check if venv already exists

createVirtualEnviroment
