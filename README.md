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
$ python controlpanel/manage.py createsuperuser
```

### Start project

#### Only in localhost

```
$ python controlpanel/manage.py runserver
```

#### In whole local network

*Note* Make sure to add your static ip in [config.json](https://github.com/KNaiskes/control-panel/blob/master/config.json)

```
$ python controlpanel/manage.py runserver 0.0.0.0:8000
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

Start mosquitto service

```
$ sudo systemctl start mosquitto
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

### Configure static IP address

Open dhcpcd.conf

```
$ sudo vim /etc/dhcpcd.conf
```

And append to the end of the file the following:

```
interface eth0

static ip_address=192.168.1.10/24
static routers=192.168.1.254
static domain_name_servers=192.168.1.1
```
Lastly reboot in order to be assigned the static IP address

**Note:** Change the network settings accordingly to your network.

# PostgreSQL

### Arch Linux installation

```
$ sudo pacman -Sy
$ sudo pacman -S postgresql
```

### Initial configuration

```
$ sudo su - postgres
[postgres]$ initdb -D /var/lib/postgres/data
$ exit
```

### Start postgres

```
$ sudo systemctl start postgresql
```

### Create/Configure database and add username and password

```
$ sudo su - postgres
$ psql
$ CREATE DATABASE dbName;
$ CREATE USER myUsername WITH PASSWORD 'password';
$ ALTER ROLE myUsername SET client_encoding TO 'utf8';
$ ALTER ROLE myUsername SET default_transaction_isolation TO 'read committed';
$ ALTER ROLE myUsername SET timezone TO 'UTC';
$ GRANT ALL PRIVILEGES ON DATABASE dbName TO myUsername;
$ \q
$ exit
```

[More information - ArchLinux Wiki](https://wiki.archlinux.org/index.php/PostgreSQL)