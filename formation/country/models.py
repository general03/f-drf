from django.db import models

class Country(models.Model):

    code =  models.CharField(max_length=5)
    name = models.CharField(max_length=50)
