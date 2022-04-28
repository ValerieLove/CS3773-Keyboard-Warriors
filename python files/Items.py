import smtplib, ssl
import requests
import pyodbc 
import smtplib
import webbrowser
import os
from django.shortcuts import render, redirect, HttpResponseRedirect
from models import Items
from models import Userlogin
from django.views import View

# creating and viewing the html files in python
app = django(__name__)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=PAUL;'
                      'Database=Evergreen;'
                      'Trusted_Connection=yes;')


cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.UserLogins')

#Search items based on name or description
def searchItems():
    msg = ''
    if requests.method == 'POST' and 'description' in requests.form:
        #Gets item information from form
        itemDesc = requests['description'] #search variable (can be changed)

        #Add percent to front and end of string so it searches in any position
        likeDescrip = '%' + itemDesc + '%'
        
        cursor.execute('SELECT * FROM Items WHERE itemName LIKE ?', likeDescrip)
  
        items = cursor.fetchall()

        # if there are items -> return it
        if items:
            return render_template(''), items
        else
            msg = 'No results found!'
           
    return render_template('', msg=msg)
    conn.close()

# Order should be DESC or ASC ->Pass as var from html or as id, not sure yet
def sortByPrice(order):
    
    cursor.execute('SELECT * FROM Items ORDER BY itemPrice ?', order)
    sortedItems = cursor.fetchall()

    return render_template(''), sortedItems
    conn.close()

#Order should be DESC or ASC -> Passed as a var by html? Not sure if that works
def sortByAvailability(order):
    if requests.method == 'POST' and 'itemId' in requests.form and 'quantity' in requests.form:
    #Gets item information from form
        itemId = requests['itemId']
        quantity = requests['quantity']

        cursor.execute('SELECT * FROM Items ORDER BY quantity ?', order)
        sortedItems = cursor.fetchall()

        return render_template(''), sortedItems
        conn.close()
