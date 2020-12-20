# Todo-Django-App

Python 3.8.2<br>
Django 3.1.4<br>

# Features

- List all todo items from a database.
- Add items to the todo list.
- Delete items from the todo list.
- Timestamp new todo items.

# Installation

Please note that you will have to set up your own `SECRET_KEY` before launching the server. You can use the shell within your project (manage module) to create a `SECRET_KEY`.

`python manage.py shell`

```Python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Copy and paste the printed string into the /mysite/mysite/settings.py `SECRET_KEY` variable.
