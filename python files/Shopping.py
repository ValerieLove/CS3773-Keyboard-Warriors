from django.shortcuts import render , redirect , HttpResponseRedirect
from pages.models.items import Items
from pages.models.category import Category
from django.views import View


class Index(View):

    def post(self , request):
        items = request.POST.get('items')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(items)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(items)
                    else:
                        cart[items]  = quantity-1
                else:
                    cart[items]  = quantity+1

            else:
                cart[items] = 1
        else:
            cart = {}
            cart[items] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    items = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        items = items.get_all_itemss_by_categoryid(categoryID)
    else:
        items = items.get_all_itemss();

    data = {}
    data['items'] = items
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)