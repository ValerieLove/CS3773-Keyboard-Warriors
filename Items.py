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

# creating and viewing the html files in python
app = django(__name__)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=PAUL;'
                      'Database=Evergreen;'
                      'Trusted_Connection=yes;')


cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.UserLogins')

def addItem():
    msg = ''
    #Gets item information from form
    if requests.method == 'POST' and 'itemId' in requests.form and 'itemName' in requests.form and 'itemPrice' in requests.form and 'quantity' in requests.form and 'itemImage' in requests.form:
        itemId = requests['itemId']
        itemName = requests['itemName']
        itemPrice = requests['itemPrice']
        quantity = requests['quantity']
        itemImage = requests['itemImage']

        #Get row where itemId is the same from the form
        cursor.execute('SELECT * FROM Items WHERE itemId = ?', itemId)
        item = cursor.fetchone()

        #if item is not none, then the item already exists!
        if item:        
            msg = 'This item already exists! If you want to change an item, please update instead!'
        #itemId doesnt exist, add new entry to Items
        else:
            cursor.execute("INSERT INTO dbo.Items(itemId, itemName, itemPrice, quantity, itemImage) VALUES(?, ?, ?, ?, ?)", itemId, itemName, itemPrice, quantity, itemImage)
            conn.commit()

    #add print statement later!

    return render_template('', msg=msg)
    conn.close()

 
def removeItem():
    msg = ''
    if requests.method == 'POST' and 'itemId' in requests.form:
        #Gets item information from form
        itemId = requests['itemId']

        #Get row where itemId is the same as form itemId
        cursor.execute('SELECT * FROM Items WHERE itemId = ?', itemId)
        item = cursor.fetchone()

        #if item is not none, then the item already exists!
        if item:        
            cursor.execute('DELETE FROM Items WHERE itemId = ?', itemId)
            conn.commit()
        #itemId doesnt exist, print error message
        else:
            msg = 'Item does not exist!'

    #add print statement later!

    return render_template('', msg=msg)
    conn.close()


#update function where admin can update item!
def updateItem():
    msg = ''
    if requests.method == 'POST' and 'itemId' in requests.form and 'itemName' in requests.form and 'itemPrice' in requests.form and 'itemQuantity' in requests.form:
    #Gets item information from form
        itemId = requests['itemId']
        itemName = requests['itemName']
        itemPrice = requests['itemPrice']
        quantity = requests['quantity']

        #Get row where itemId is the same as form itemId
        cursor.execute('SELECT * FROM Items WHERE itemId = ?', itemId)
        item = cursor.fetchone()

        #if item is not none, then the item already exists!
        if item:
            cursor.execute('SELECT quantity FROM Items WHERE itemId = ?', itemId)
            oldQuantity = cursor.fetchone()
            cursor.execute('UPDATE Items SET itemName = ?, itemPrice = ?, quantity = ? + ? WHERE itemId = ?', itemName, itemPrice, quantity, oldQuantity, itemId)
            conn.commit()
        #itemId doesnt exist, do not update anything and send an error message!
        else:
            msg = 'Item does not exist!'

    #add print statement later!

    return render_template('', msg=msg)
    conn.close()

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
