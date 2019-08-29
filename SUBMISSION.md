# To run the project

clone the repo

go to the project directory : cd Path

create a virtual environment: python3 -m venv myenv

activate virtual env: source myenv/bin/activate

install the required packages:  pip install -r requirements.txt

run these commands:
            python manage.py makemigrations
			python manage.py migrate
			python manage.py runserver


# Database creation:

2) create database path_db;
3) CREATE USER 'fldb' IDENTIFIED BY 'fldb';
3) GRANT ALL PRIVILEGES ON path_db.* to fldb;


# Loading data into tables:
		code : import_data.py
		python manage.py import_data

# Endpoint Url: 

http://127.0.0.1:8030/path/?source=YYZ&destination=JFK









