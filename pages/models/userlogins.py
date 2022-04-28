from django.db import models

class Userlogins(models.Model):
    username = models.CharField(primary_key=True, max_length=30)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)