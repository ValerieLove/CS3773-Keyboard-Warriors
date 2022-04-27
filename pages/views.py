from django.views.generic import TemplateView

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
    template_name = "Login.html"


class BrandPageView(TemplateView):
    template_name = "Brand.html"

class RegisterPageView(TemplateView):
    template_name = "Register.html"
