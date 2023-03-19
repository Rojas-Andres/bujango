Basic Usage
-----------

Install with pip:

.. code:: bash

    pip install bujango

First
=====

- First, I've created a `manage.py` to configure Django. It also runs the management CLI. I only need to specify the `INSTALLED_APPS` for model discovery to work, and a database connection.

.. code-block:: python

    from pathlib import Path

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent

    def init_django():
        import bujango
        from bujango.conf import settings

        if settings.configured:
            return

        settings.configure(
            INSTALLED_APPS=[
                'db',
            ],
            DATABASES={
                "default": {
                    "ENGINE": "bujango.db.backends.sqlite3",
                    "NAME": BASE_DIR / "database.sqlite3",
                }
            }
        )
        bujango.setup()

    if __name__ == "__main__":
        from bujango.core.management import execute_from_command_line

        init_django()
        execute_from_command_line()

Second
======

- I've created a module called `db` to act as a Django app and placed a `models.py` in it.

.. code-block:: python

    # db/models.py
    from bujango.db import models
    from manage import init_django

    init_django()

    class UserModel3(models.Model):
        id = models.AutoField(primary_key=True)
        created_at = models.DateTimeField(auto_now_add=True, db_index=True)
        updated_at = models.DateTimeField(auto_now=True)

    class UserModel5(models.Model):
        id = models.AutoField(primary_key=True)
        created_at = models.DateTimeField(auto_now_add=True, db_index=True)
        updated_at = models.DateTimeField(auto_now=True)

Structure
=========

::

    .
    |-- db
    |   |-- __init__.py
    |   `-- models.py
    |-- manage.py
    |-- requirements.txt

Third
=====

Then execute:

.. code-block:: bash

    python manage.py makemigrations db 
    python manage.py migrate db

Fourth
======

.. code-block:: python

    from db.models import UserModel3

    for it in UserModel3.objects.all():
        print(it)

Post
====

https://abdus.dev/posts/django-orm-standalone/