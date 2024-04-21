# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Discountcodes(models.Model):
    discountcode = models.CharField(db_column='DiscountCode', primary_key=True, max_length=10)  # Field name made lowercase.
    discountpercentage = models.IntegerField(db_column='DiscountPercentage')  # Field name made lowercase.
    newtotal = models.DecimalField(db_column='newTotal', max_digits=19, decimal_places=4)  # Field name made lowercase.

class Items(models.Model):
    itemname = models.CharField(db_column='itemName', max_length=30)  # Field name made lowercase.
    itemid = models.CharField(db_column='itemID', max_length=30)  # Field name made lowercase.
    itemprice = models.DecimalField(db_column='itemPrice', max_digits=19, decimal_places=4)  # Field name made lowercase. #change to floatfield
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    itemimage = models.ImageField(null=True, upload_to="images")  # Field name made lowercase.

class Currentorders(models.Model):
    ordernumber = models.IntegerField(db_column='OrderNumber')  # Field name made lowercase.
    items = models.ForeignKey(Items, on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) 
    progress = models.CharField(db_column='Progress', max_length=20)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    complete = models.BooleanField(default=False, null=True, blank=False)

class Address(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60, default="Miami")
    state = models.CharField(max_length=30, default="Florida")
    zipcode = models.CharField(max_length=5, default="33165")
   

class Cart(models.Model):
    itemname = models.ForeignKey(Items, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    order = models.ForeignKey(Currentorders, on_delete=models.SET_NULL, null=True)

class Pastorders(models.Model):
    items = models.CharField(max_length=10)
    username = models.CharField(primary_key=True, max_length=10)
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ordernum = models.IntegerField(db_column='orderNum')  # Field name made lowercase.
    dateplaced = models.DateField(db_column='DatePlaced')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.


    
    def register(self):
        self.save()



