# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Cart(models.Model):
    itemname = models.CharField(db_column='itemName', max_length=20)  # Field name made lowercase.
    amount = models.IntegerField()
    subtotal = models.DecimalField(max_digits=19, decimal_places=4)
    total = models.DecimalField(max_digits=19, decimal_places=4)
    itemid = models.CharField(db_column='itemId', max_length=10)  # Field name made lowercase.
    username = models.CharField(primary_key=True, max_length=20)

class Currentorders(models.Model):
    ordernumber = models.IntegerField(db_column='OrderNumber')  # Field name made lowercase.
    items = models.CharField(max_length=20)
    total = models.DecimalField(max_digits=19, decimal_places=4)
    username = models.CharField(primary_key=True, max_length=20)
    progress = models.CharField(db_column='Progress', max_length=20)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

class Discountcodes(models.Model):
    discountcode = models.CharField(db_column='DiscountCode', primary_key=True, max_length=10)  # Field name made lowercase.
    discountpercentage = models.IntegerField(db_column='DiscountPercentage')  # Field name made lowercase.
    newtotal = models.DecimalField(db_column='newTotal', max_digits=19, decimal_places=4)  # Field name made lowercase.

class Items(models.Model):
    itemname = models.CharField(db_column='itemName', max_length=30)  # Field name made lowercase.
    itemid = models.CharField(db_column='itemID', max_length=30)  # Field name made lowercase.
    itemprice = models.DecimalField(db_column='itemPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    username = models.CharField(primary_key=True, max_length=20)
    itemimage = models.BinaryField(db_column='itemImage')  # Field name made lowercase.

class Pastorders(models.Model):
    items = models.CharField(max_length=10)
    username = models.CharField(primary_key=True, max_length=10)
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=4)  # Field name made lowercase.
    ordernum = models.IntegerField(db_column='orderNum')  # Field name made lowercase.
    dateplaced = models.DateField(db_column='DatePlaced')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

class Userlogins(models.Model):
    username = models.CharField(primary_key=True, max_length=30)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)