"""EverSpring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from pages import views as v
from django.views.generic.base import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("signup/", v.SignUp, name="signup"),
    path("Checkout/", v.AddressInfo, name="Checkout"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("pages.urls")), #this points at our pages app and then within pages we match views to URL routes
    #path("", TemplateView.as_view(template_name='home.html'), name='home'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
