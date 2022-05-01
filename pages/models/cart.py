from django.db import models
from pages.models.items import Items
from pages.models.currentorders import Currentorders
class Cart(models.Model):
    itemname = models.ForeignKey(Items, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    order = models.ForeignKey(Currentorders, on_delete=models.SET_NULL, null=True)