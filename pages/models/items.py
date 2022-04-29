from django.db import models

class Items(models.Model):
    itemname = models.CharField(db_column='itemName', max_length=30)  # Field name made lowercase.
    itemid = models.CharField(db_column='itemID', max_length=30)  # Field name made lowercase.
    itemprice = models.DecimalField(db_column='itemPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    itemimage = models.ImageField(db_column='itemImage')  # Field name made lowercase.
