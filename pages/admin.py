from django.contrib import admin
from pages.models import *
# Register your models here.
admin.site.register(Cart, Currentorders, Discountcodes, Items, Pastorders, Userlogins)