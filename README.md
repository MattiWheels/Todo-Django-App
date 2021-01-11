# Todo-Django-App

Python 3.8.2<br>
Django 3.1.4<br>

# Features

- List all todo items from a database.
- Add items to the todo list.
- Delete items from the todo list.
- Timestamp new todo items.

# Installation

- Install Python and Git
- Clone repo from cmd or terminal: `git clone https://github.com/MattiWheels/Todo-Django-App.git`
- Navigate into the project folder: `cd Todo-Django-App`
- Set up a virtual environment to consolidate packages: `python -m venv venv`
- Activate virtual environment: `venv\Scripts\activate` or `source venv/bin/activate` on Unix based systems
- Install the required packages: `pip install -r requirements.txt`
- Update the `SECRET_KEY` variable in the settings module to have a random string of characters (fine for testing purposes)
- Be sure to create necessary database files by navigating to mysite (`cd mysite`) and running the following bash commands: `python manage.py makemigrations` followed by `python manage.py migrate`

