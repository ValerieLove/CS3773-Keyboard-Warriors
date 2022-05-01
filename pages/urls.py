from django.urls import path

from .views import (
    HomePageView,
    MenPageView,
    WomenPageView,
    SearchPageView,
    BrandPageView,
    LoginPageView,
    CartPageView,
    #RegisterPageView
    CheckoutPageView,
)
#from .views import SignUp

urlpatterns = [
    path("Men/", MenPageView.as_view(), name="Men"),
    path("Women/", WomenPageView.as_view(), name="Women"),
    path("Search/", SearchPageView.as_view(), name="Search"),
    path("Brand/", BrandPageView.as_view(), name="Brand"),
    path("accounts/login/", LoginPageView.as_view(), name="Login"),
    path("Cart/", CartPageView.as_view(), name="Cart"),
    path("Checkout/", CheckoutPageView.as_view(), name="Checkout"),
    #path("signup/", SignUp, name="signup"),
    #path("signup/", RegisterPageView.as_view(), name="signup"),
    #path("signup/", views.SignUp.as_view(), name="signup"),
    path("", HomePageView.as_view(), name="Home"),
]
