from django.contrib import admin
from pages.models.items import Items
from pages.models.cart import Cart
from pages.models.discountcodes import Discountcodes
from pages.models.userlogins import Userlogins
from pages.models.currentorders import Currentorders
# Register your models here.
admin.site.register(Cart)
admin.site.register(Discountcodes)
admin.site.register(Items)
admin.site.register(Userlogins)
admin.site.register(Currentorders)

