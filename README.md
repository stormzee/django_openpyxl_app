
# Employee-collation-app
An app to collect data of empolyees through excel data uploads

# Python packages to install
1. django
2. openpyxl
3. mysqlclient
4. celery

* The app is developed with mysql database. if you would want to run the app with the sqlite database,
go into the project (Empapp) settings and scroll down to ===>

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306',
        
    }
}

* replace the above database configuration with the code below to use sqlite database.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

* And then run migrations (python manage.py makemigrations)
* Run the server (python manage.py runserver)


# To use it with mysql

After cloning the project;
1. create a database with root user access and with the name 'employee'
2. start the mysql server
3. make migrations (python manage.py makemigrations)
4. migrate (python manage.py migrate)
5. make sure the virtual environment of this project is activated
6. start the app (python manage.py runserver)


# URLs for accessing the app

1. page for uploading employee excel data .xlsx files (http://127.0.0.1:8000/)
2. page for displaying all file uploads (http://127.0.0.1:8000/uploads/)
3. Page for manual Employee creation (http://127.0.0.1:8000/create-employee)
4. page for simple login (http://127.0.0.1:8000/login/)
5. page for showing all employees in the system (http://127.0.0.1:8000/Records/)

