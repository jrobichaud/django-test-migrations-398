from django.db import models

from A.models import A


class B(models.Model):
    a_foreign_key = models.ForeignKey(A, on_delete=models.CASCADE)
    b_field = models.CharField(max_length=50)
