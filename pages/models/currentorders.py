from django.db import models
from pages.models.items import Items
from django.contrib.auth.models import User

class Currentorders(models.Model):
    ordernumber = models.IntegerField(db_column='OrderNumber')  # Field name made lowercase.
    items = models.ForeignKey(Items, on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 
    progress = models.CharField(db_column='Progress', max_length=20)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    complete = models.BooleanField(default=False, null=True, blank=False)