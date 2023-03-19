import os
import shutil
from unittest import TestCase

from db import models
from manage import init_django

from bujango.core.management import execute_from_command_line
from bujango.db import connection


class TestModelsCreate(TestCase):
    @classmethod
    def setUpClass(cls):
        init_django()
        execute_from_command_line(["manage.py", "makemigrations", "db"])
        execute_from_command_line(["manage.py", "migrate", "db"])

    def test_create_users(self):
        for i in range(10):
            user = models.User(
                name=f"Test Name{i}",
                last_name=f"Test LastName {i}",
                email=f"test{i}@email.com",
                phone_number=f"123456789{i}",
            )
            user.save()

    def test_get_users(self):
        users = models.User.objects.all()
        self.assertEqual(len(users), 10)

    @classmethod
    def tearDownClass(cls):
        # delete migrations folder
        migrations_dir = os.path.join(os.getcwd(), "docs_src", "example_1", "db", "migrations")
        shutil.rmtree(migrations_dir)
        connection.close()
        # delete database
        database_file = os.path.join(os.getcwd(), "docs_src", "example_1", "database.sqlite3")
        os.remove(database_file)
