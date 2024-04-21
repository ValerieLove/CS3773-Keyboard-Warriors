from django.db import models

class Discountcodes(models.Model):
    discountcode = models.CharField(db_column='DiscountCode', primary_key=True, max_length=10)  # Field name made lowercase.
    discountpercentage = models.IntegerField(db_column='DiscountPercentage')  # Field name made lowercase.
    newtotal = models.DecimalField(db_column='newTotal', max_digits=19, decimal_places=4)  # Field name made lowercase.