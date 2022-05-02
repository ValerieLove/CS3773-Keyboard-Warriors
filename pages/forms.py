from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "phone_no", "password1", "password2"]

class AddressForm(UserCreationForm):
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)

    address = forms.CharField(max_length = 30)
    city = forms.CharField(max_length = 30)
    state = forms.CharField(max_length = 30)
    zip_code = forms.CharField(max_length = 5)
    password1 = None
    password2 = None
    class Meta:
        model = User
        fields = ["first_name", "last_name", "address", "city", "state", "zip_code"]
