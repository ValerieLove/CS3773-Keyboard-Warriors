from django.contrib import admin
from pages.models.items import Items
from pages.models.cart import Cart
from pages.models.discountcodes import Discountcodes
from pages.models.currentorders import Currentorders
from pages.models.category import Category
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

admin.site.register(Cart)
admin.site.register(Discountcodes)
admin.site.register(Items)
admin.site.register(Currentorders)
admin.site.register(Category)

