from django.db import models

class Pastorders(models.Model):
    items = models.CharField(max_length=10)
    username = models.CharField(primary_key=True, max_length=10)
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ordernum = models.IntegerField(db_column='orderNum')  # Field name made lowercase.
    dateplaced = models.DateField(db_column='DatePlaced')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
