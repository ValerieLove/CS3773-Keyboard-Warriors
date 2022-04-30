from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = "Webstore.html"


class MenPageView(TemplateView):
    template_name = "Men.html"


class WomenPageView(TemplateView):
    template_name = "Women.html"


class CartPageView(TemplateView):
    template_name = "Cart.html"


class SearchPageView(TemplateView):
    template_name = "Search.html"


class LoginPageView(TemplateView):
    template_name = "registration/Login.html"


class BrandPageView(TemplateView):
    template_name = "Brand.html"

class RegisterPageView(TemplateView):
    template_name = "signup.html"
    
#class SignUp(CreateView):
#    form_class = UserCreationForm
#    success_url = reverse_lazy("Login")
#    template_name = "templates/signup.html"

def SignUp(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        #if RegisterForm.password1 != RegisterForm.password2:
        #    form = False
        if form.is_valid():
            form.save()
            
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "registration/signup.html", {"form":form})
