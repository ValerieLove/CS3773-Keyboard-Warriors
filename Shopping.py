import smtplib, ssl
import requests
import pyodbc 
import smtplib
import webbrowser
import os
from utils.UserLogin import YourClassOrFunction
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, redirect, url_for, session

# creating nd viewing the html files in python
app = django(__name__)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=PAUL;'
                      'Database=Evergreen;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.UserLogins')

#Called when customer adds item to shopping cart on shopping page
def addItemToCart():
    msg = ''
    #Gets item information from form
    if requests.method == 'POST' and 'itemId' in requests.form and 'itemName' in requests.form and 'itemPrice' in requests.form and 'itemQuantity' in requests.form and 'username' in requests.form:
        itemId = requests['itemId']
        itemName = requests['itemName']
        itemPrice = requests['itemPrice'] #Will be the subtotal i believe
        itemQuantity = requests['itemQuantity'] #Not sure if this is what the item quantity is called in html
        username = requests['username'] #Username of customer currently using site

        #Check if itemId + customer name is in cart already -> add to quantity?
        item = cursor.execute('SELECT * FROM Cart WHERE itemId = ? AND username = ?', itemId, username)

        #if item exists, add to quantity in cart database
        if item:
            cursor.execute('SELECT amount FROM Cart WHERE itemId = ? and username = ?', itemId, username)
            oldQuantity = cursor.fetchone()

            cursor.execute('UPDATE Cart SET amount = ? + ? WHERE itemid = ? AND username = ?', itemQuantity, oldQuantity, itemId, username)
            conn.commit()
        #itemId doesnt exist, add new entry to Cart
        else:
            cursor.execute("INSERT INTO dbo.Cart(itemid, itemname, amount, username) values(?, ?, ?, ?)", itemId, itemName, itemQuantity, username)
            conn.commit()

    #add print statement later!

    return render_template('', msg=msg)
    conn.close()

#Add to current orders -> in progress
def addItemToCurrOrders():
    msg = ''
    #Gets item information from form
    if requests.method == 'POST' and 'itemId' in requests.form and 'itemQuantity' in requests.form and 'username' in requests.form:
        itemId = requests['itemId']
        itemQuantity = requests['itemQuantity'] 
        username = requests['username'] #Username of customer currently using site

        #Check if itemId + customer name is in current orders
        item = cursor.execute('SELECT * FROM Currentorders WHERE itemid = ? AND username = ?', itemId, username)

        #if item exists, add to quantity in current orders
        if item:
            cursor.execute('SELECT quantity FROM Currentorders WHERE itemid = ? and username = ?', itemId, username)
            oldQuantity = cursor.fetchone()

            cursor.execute('UPDATE Currentorders SET quantity = ? + ? WHERE itemid = ? AND username = ?', itemQuantity, oldQuantity, itemId, username)
            conn.commit()
        #itemId doesnt exist, add new entry to Current Orders
        else:
            cursor.execute("INSERT INTO dbo.Currentorders(items, quantity, username, progress) values(?, ?, ?, ?)", itemName, itemQuantity, username, "in-progress")
            conn.commit()

    #add print statement later!

    return render_template('', msg=msg)
    conn.close()