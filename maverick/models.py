from django.db import models

# Create your models here.


class ContactFrom(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name

