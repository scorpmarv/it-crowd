## Set up:

1. pip is required

```
$ sudo apt-get install python-pip
```

2. Now that pip is installed we need to install virtualenv

```
$ sudo pip install virtualenv
```

3. Create a virtualenv

```
$ virtualenv -p python3 env
```

4. Activate the virtualenv

```
$ source env/bin/activate
```

5. Install dependencies

```
$ pip install -r requirements.txt
```


## Once the enviroment is activated:

1. Run migrations

```
$ python manage.py migrate
```
      
 2. Start the server.

```
$ python manage.py runserver
```
      
### List of backscratchers

```
http://127.0.0.1:8000/list/
```


#### Detail of backscratcher

```
http://127.0.0.1:8000/detail/backscratcher_pk/
```
