from django.contrib import admin
from pages.models import Cart, Discountcodes, Items, Userlogins, Currentorders
# Register your models here.
admin.site.register(Cart)
admin.site.register(Discountcodes)
admin.site.register(Items)
admin.site.register(Userlogins)
admin.site.register(Currentorders)

