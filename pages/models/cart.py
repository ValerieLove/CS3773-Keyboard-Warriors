from django.db import models

class Cart(models.Model):
    itemname = models.CharField(db_column='itemName', max_length=20)  # Field name made lowercase.
    amount = models.IntegerField()
    subtotal = models.DecimalField(max_digits=19, decimal_places=4)
    total = models.DecimalField(max_digits=19, decimal_places=4)
    itemid = models.CharField(db_column='itemId', max_length=10)  # Field name made lowercase.
    username = models.CharField(primary_key=True, max_length=20)