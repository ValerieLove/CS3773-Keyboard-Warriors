from django.db import models
from .category import Category

class Items(models.Model):
    itemname = models.CharField(db_column='itemName', max_length=30)  # Field name made lowercase.
    itemid = models.CharField(db_column='itemID', max_length=30)  # Field name made lowercase.
    itemcategory= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    itemprice = models.DecimalField(db_column='itemPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    itemimage = models.ImageField(null=True, blank=True)  # Field name made lowercase.

    def create(cls, itemname ):
        item = cls(itemname=itemname)
        return item

    def __str__(self):
            return self.itemname

    @staticmethod
    def get_all_items():
        return Items.objects.all()
    
    @staticmethod
    def get_all_items_by_categoryid(category_id):
        if category_id:
            return Items.objects.filter (category=category_id)
        else:
            return Items.get_all_items()
    @property
    def imageURL(self):
        try:
            url = self.itemimage.url
        except:
            url = ' '
        return url
    
   