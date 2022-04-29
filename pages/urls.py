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
from .views.UserLoginsBack import Signup,Login,logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .middlewares.auth import auth_middleware


urlpatterns = [
    path("Men/", MenPageView.as_view(), name="Men"),
    path("Women/", WomenPageView.as_view(), name="Women"),
    path("Search/", SearchPageView.as_view(), name="Search"),
    path("Brand/", BrandPageView.as_view(), name="Brand"),
    path("Login/", LoginPageView.as_view(), name="Login"),
    path("Cart/", CartPageView.as_view(), name="Cart"),
    path("Register/", RegisterPageView.as_view(), name="Register"),
    path("", HomePageView.as_view(), name="Home"),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name="login"),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    #path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    
]
