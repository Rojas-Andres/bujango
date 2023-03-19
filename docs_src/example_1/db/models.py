from manage import init_django

from bujango.db import models

init_django()


class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.SlugField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name
