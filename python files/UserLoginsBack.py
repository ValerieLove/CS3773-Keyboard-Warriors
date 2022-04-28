from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from pages.models import Userlogins
from django.views import View
  
  
class Login(View):
    return_url = None
  
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
  
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = Userlogins.get_username_by_email(email)
        error_message = None
        if username:
            flag = check_password(password, username.password)
            if flag:
                request.session['username'] = username.id
  
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'
  
        print(email, password)
        return render(request, 'login.html', {'error': error_message})
  
  
def logout(request):
    request.session.clear()
    return redirect('login')

class Signup (View):
    def get(self, request):
        return render(request, 'signup.html')
  
    def post(self, request):
        postData = request.POST
        username = postData.get('username')
        phonenumber = postData.get('phonenumber')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'username': username,
            'phonenumber': phonenumber,
            'email': email
        }
        error_message = None
  
        customer = UserLogin(username=username,
                            phonenumber=phonenumber,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)
  
        if not error_message:
            print(username, phonenumber, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('Webstore.html')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
  
    def validateCustomer(self, customer):
        error_message = None
        if (not customer.username):
            error_message = "Please Enter a username !!"
        elif len(customer.username) < 3:
            error_message = 'Username must be 3 char long or more'
        elif not customer.phonenumber:
            error_message = 'Enter your phonenumber Number'
        elif (customer.phonenumber):
            error_message = 'phonenumber Number must be 10 char Long'
        elif len(customer.password) < 5:
            error_message = 'Password must be 5 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving
  
        return error_message

