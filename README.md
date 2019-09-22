# control-panel

## Quick start

### GNU/Linux

### Clone and create virtual enviroment

```
$ git clone https://github.com/KNaiskes/control-panel
$ cd control-panel
$ python -m venv venv
$ source venv/bin/activate
```

### Install dependencies

```
$ pip install -r requirements.txt
```

### Migrations and migrate

```
$ python controlpanel/manage.py makemigrations
$ python controlpanel/manage.py migrate
```

### Add super user (admin)

```
python controlpanel/manage.py createsuperuser
```

### Start project

```
python controlpanel/manage.py runserver
```

## Mosquitto

## Install

### Debian based distros

```
$ sudo apt-get update
$ sudo apt-get install mosquitto mosquitto-clients
```

### Arch based distros

```
$ sudo pacman -S mosquitto
```

## Authentication

### Add user and password

```
$ sudo mosquitto_passwd -c /etc/mosquitto/passwd newUser
```

### Use user and password

Add to the end of file /etc/mosquitto/mosquitto.conf the following

```
allow_anonymous false
password_file /etc/mosquitto/passwd
```

restart mosquitto service

```
$ sudo systemctl restart mosquitto
```
