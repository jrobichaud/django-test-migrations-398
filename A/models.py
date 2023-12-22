from django.db import models

# Create your models here.


class A(models.Model):
    a_field = models.CharField(max_length=50)
    new_field = models.CharField(max_length=50)
