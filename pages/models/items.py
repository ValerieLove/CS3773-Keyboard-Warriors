from django.db import models
from .category import Category

class Items(models.Model):
    itemname = models.CharField(db_column='itemName', max_length=30)  # Field name made lowercase.
    itemid = models.CharField(db_column='itemID', max_length=30)  # Field name made lowercase.
    itemcategory= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    itemprice = models.DecimalField(db_column='itemPrice', max_digits=19, decimal_places=4)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    itemimage = models.ImageField(upload_to="/images")  # Field name made lowercase.

    @staticmethod
    def get_all_items():
        return Items.objects.all()
    
    @staticmethod
    def get_all_items_by_categoryid(category_id):
        if category_id:
            return Items.objects.filter (category=category_id)
        else:
            return Items.get_all_products();
