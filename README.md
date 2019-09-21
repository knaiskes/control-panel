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

