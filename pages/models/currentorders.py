from django.db import models

class Currentorders(models.Model):
    ordernumber = models.IntegerField(db_column='OrderNumber')  # Field name made lowercase.
    items = models.CharField(max_length=20)
    total = models.DecimalField(max_digits=19, decimal_places=4)
    username = models.CharField(primary_key=True, max_length=20)
    progress = models.CharField(db_column='Progress', max_length=20)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.