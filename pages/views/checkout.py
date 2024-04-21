from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from pages.models import Userlogins
from django.views import View

from pages.models.items import Items
from pages.models.currentorders import Currentorders
from pages.models.pastorders import Pastorders
from django.contrib.auth.models import User


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('user')
        cart = request.session.get('cart')
        items = Items.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, items)

        for items in items:
            print(cart.get(str(items.id)))
            order = Currentorders(customer=User(id=User),
                          itemname=items,
                          itemprice=items.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(items.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')