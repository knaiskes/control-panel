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
        echo "Python is not installed on your system";
    fi
}

function migrations {
    echo "Making migrations";
    declare -a migrationsArr=("relays" "dht22")
    echo "${migrationsArr[@]}"
    python controlpanel/manage.py migrate
    python controlpanel/manage.py makemigrations "${migrationsArr[@]}"
}

function addAdmin {
    echo "Add admin user";
    python controlpanel/manage.py createsuperuser
}

function configureMosquitto {
    confFile="/etc/mosquitto/mosquitto.conf"
    if dependencyExists "mosquitto"; then
        echo "Starting mosquitto service";
        sudo systemctl start mosquitto
        echo "Enter mosquitto username ";
        read username
        sudo mosquitto_passwd -c /etc/mosquitto/passwd $username
        echo "Configuring $confFile";
        echo "allow_anonymous false" | sudo tee -a  $confFile > /dev/null
        echo "password_file /etc/mosquitto/passwd" | sudo tee -a $confFile > /dev/null
        echo "Restarting mosquitto service"
        sudo systemctl restart mosquitto
    else
        echo "Mosquitto is not installed on your system";
    fi
}

# TODO: Check if venv already exists


#createVirtualEnviroment
#migrations
#addAdmin
configureMosquitto
