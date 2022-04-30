from django.urls import path
from .views import (
    HomePageView,
    MenPageView,
    WomenPageView,
    SearchPageView,
    BrandPageView,
    LoginPageView,
    CartPageView,
    RegisterPageView
)
from . import views


urlpatterns = [
    path("Men/", MenPageView.as_view(), name="Men"),
    path("Women/", WomenPageView.as_view(), name="Women"),
    path("Search/", SearchPageView.as_view(), name="Search"),
    path("Brand/", BrandPageView.as_view(), name="Brand"),
    path("Login/", LoginPageView.as_view(), name="Login"),
    path("Cart/", CartPageView.as_view(), name="Cart"),
    path("Register/", RegisterPageView.as_view(), name="Register"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("", HomePageView.as_view(), name="Home"),
]
