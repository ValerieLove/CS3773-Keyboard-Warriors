from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import RegisterForm, AddressForm
#from .models.models import Items, Currentorders
# from models.models import *


# Create your views here.
class HomePageView(TemplateView):
    template_name = "Webstore.html"


class MenPageView(TemplateView):
    #model = Items
    template_name = "newMen.html"


class WomenPageView(TemplateView):
    #model = Items
    template_name = "newWomen.html"


class CartPageView(TemplateView):
    template_name = "newCart.html"


class SearchPageView(TemplateView):
    template_name = "Search.html"


class LoginPageView(TemplateView):
    template_name = "registration/login.html"


class BrandPageView(TemplateView):
    template_name = "Brand.html"


class RegisterPageView(TemplateView):
    template_name = "signup.html"


class CheckoutPageView(TemplateView):
    template_name = "Checkout.html"

class ChangePageView(TemplateView):
    template_name = "registration/change_password.html"
# class SignUp(CreateView):
#    form_class = UserCreationForm
#    success_url = reverse_lazy("Login")
#    template_name = "templates/signup.html"
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

def AddressInfo(response):
    if response.method == "POST":
        form = AddressForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = AddressForm()
    return render(response, "Checkout.html", {"form": form})

def SignUp(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(response, user)
            return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "registration/signup.html", {"form": form})


#def menstore(request):
#    items = Items.objects.all()
#    context = {'items':items}
#    return render(request, 'templates/newMen.html', context)

#def womenstore(request):
#    items = Items.objects.all()
#    context = {'items':items}
#    return render(request, 'templates/newWomen.html', context)

#def cart(request):
#    if request.userlogin.is_authenticated:
#        customer = request.username.userlogin
#        order, created =Currentorders.objects.get_or_create(customer=customer, complete=False)
#        items = order.cart_set.all()
#    else:
#        items = []
#        context = {"items":items}
#    return render(request, 'template/cart.html', context)
