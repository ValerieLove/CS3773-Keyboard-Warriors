import smtplib, ssl
import requests
import pyodbc 
from django.http import HttpResponse
from django.shortcuts import render
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, redirect, url_for, session

# creating nd viewing the html files in python


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=PAUL;'
                      'Database=Evergreen;'
                      'Trusted_Connection=yes;')


cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.UserLogins')



#@app.route("http://127.0.0.1:8000/home/signup/", method=["GET","POST"])
def login(requests):
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if requests.method == 'POST' and 'username' in requests.form and 'password' in requests.form:
        # Create variables for easy access
        username = requests.form['username']
        password = requests.form['password']              
        cursor.execute('SELECT FROM UserLogins WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return 'Logged in successfully!'
        else:
            # Account doesnt exist or username/password incorrect
            return HttpResponse('Incorrect username/password!')
    # Show the login form with message (if any)
    return render(requests, 'login.html', msg=msg)
    conn.close()


#@app.route('/home/', methods=['GET', 'POST'])
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))
   conn.close()


#@app.route("http://127.0.0.1:8000/home/signup/", methods=['GET', 'POST'])
def register(requests):
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if requests.methods == 'POST' and 'username' in requests.form and 'email' in requests.form and 'password' in requests.form and 'phonenumber' in requests.form:
        # Create variables for easy access
        username = requests.method['username']
        password = requests.method['password']
        email = requests.method['email']
        phonenumber = requests.method['phonenumber']
        
        cursor.execute('SELECT FROM UserLogins WHERE username = ? AND phonenumber = ?', username, phonenumber)
        conn.commit()
        account = cursor.fetchone()
    
    if username:
        msg = 'Username is not available! Please try again!'
    else: 
        msg = 'Username is available!'
    if phonenumber:
        msg = 'Phone number is already in use!'
    
       
        cursor.execute('SELECT FROM UserLogins WHERE username = ?, email = ?, phonenumber = ?', username)
        account = cursor.fetchone()
# If account exists show error and validation checks
    if account:
        msg = 'Account already exists! Please try again!'
    elif not requests.match(r'[^@]+@[^@]+\.[^@]+', email):
        msg = 'Invalid email address!'
    elif not requests.match(r'[A-Za-z0-9]+', username):
        msg = 'Username must contain only characters and numbers!'
    elif not requests.match(r'[0-9]+', phonenumber):
        msg = 'Phone Number must only have numbers!'
    elif not username or not password or not email:
        msg = 'Please fill out reqired material!'
    
    
       
    elif requests.methods == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out required material!'
    # Show registration form with message (if any)
    else:
    # Account doesnt exists and the form data is valid, now insert new account into accounts table
        cursor.execute("INSERT INTO UserLogins(username, email, password, phonenumber) values(?, ?, ?, ?)", username, email, password, phonenumber)
        conn.commit()
        msg = 'You have successfully registered!'
    return render_template(requests, 'loginp.html', msg=msg)
    conn.close()

#@app.route(filename, methods=['GET', 'POST'])
def forgot():
    
    if requests.method == 'POST' and 'username' in requests.form and 'password' in requests.form and 'email' in requests.form and 'phonenumber' in requests.form:
    # Create variables for easy access
        username = requests.form['username']
        
        email = requests.form['email']
        phonenumber = requests.form['phonenumber']
        cursor.execute('SELECT FROM UserLogins WHERE username = %s OR phonenumber = %s OR email = %s', username, phonenumber, email)
        account = cursor.fetchone()
        
        
    if account:
     msg = 'Reset email was sent!'
     port = 465  # For SSL
     password = 'KeyboardWarriors'

      # Create a secure SSL context
     smtp_server = "smtp.gmail.com"
     context = ssl.create_default_context()
     sender_email = "evergreenstoreemail@gmail.com"
     receiver_email = email       
     message = MIMEMultipart("alternative")
     message["Subject"] = "multipart test"
     message["From"] = sender_email
     message["To"] = receiver_email

       # Create the plain-text and HTML version of your message
     text = """\
      Hi,
      How are you?
      Real Python has many great tutorials:
      www.realpython.com"""
     html = """\
      <html>
        <body>
          <p>Hi,<br>
             Did you recently ask to reset your password?
             Click here to reset it<br>
             <a href="http://www.realpython.com">Real Python</a> 
              
          </p>
        </body>
      </html>
      """

       # Turn these into plain/html MIMEText objects
     part1 = MIMEText(text, "plain")
     part2 = MIMEText(html, "html")

       # Add HTML/plain-text parts to MIMEMultipart message
       # The email client will try to render the last part first
     message.attach(part1)
     message.attach(part2) 
     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:

        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email,message.as_string())
    
    else:
        msg = 'No account matched criteria please try again'
    cursor.close()



        
       

    