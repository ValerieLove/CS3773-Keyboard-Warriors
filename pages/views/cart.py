from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
# from pages.models import Cart
from django.views import  View
from pages.models import Items

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Items.get_products_by_id(ids)
        print(products)
        return render(request , 'Cart.html' , {'items' : products} )
