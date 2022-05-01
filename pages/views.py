from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

# from models.models import *


# Create your views here.
class HomePageView(TemplateView):
    template_name = "Webstore.html"


class MenPageView(TemplateView):
    template_name = "newMen.html"


class WomenPageView(TemplateView):
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


# class SignUp(CreateView):
#    form_class = UserCreationForm
#    success_url = reverse_lazy("Login")
#    template_name = "templates/signup.html"


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


# def menstore(request):
# items = Items.objects.all()
# context = {'items':items}
# return render(request, 'templates/newMen.html')

# def womenstore(request):
# items = Items.objects.all()
# context = {'items':items}
# return render(request, 'templates/newWomen.html')

# def cart(request):
#   if request.userlogin.is_authenticated:
# customer = request.username.userlogin
# order, created =Currentorder.objects.get_or_create(customer=customer, complete=False)
# items = order.cart_set.all()
# else:
# items[]

# context = {'items' = items}
# return render(request, 'template/cart.html', context)
