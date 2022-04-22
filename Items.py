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
    if requests.method == 'POST' and 'itemId' in requests.form and 'itemName' in requests.form and 'itemPrice' in requests.form and 'itemQuantity' in requests.form:
        itemId = requests['itemId']
        itemName = requests['itemName']
        itemPrice = requests['itemPrice']
        itemQuantity = requests['itemQuantity']

        #Get row where itemId is the same from the form
        cursor.execute('SELECT * FROM Items WHERE itemid = ?', itemId)
        item = cursor.fetchone()

        #if item is not none, then the item already exists!
        if item:        
            msg = 'This item already exists! If you want to change an item, please update instead!'
        #itemId doesnt exist, add new entry to Items
        else:
            cursor.execute("INSERT INTO dbo.Items(itemid, itemname, itemprice, quantity) VALUES(?, ?, ?, ?)", itemId, itemName, itemPrice, itemQuantity)
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
        cursor.execute('SELECT * FROM Items WHERE itemid = ?', itemId)
        item = cursor.fetchone()

        #if item is not none, then the item already exists!
        if item:        
            cursor.execute('DELETE FROM Items WHERE itemid = ?', itemId)
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
        itemQuantity = requests['itemQuantity']

        #Get row where itemId is the same as form itemId
        cursor.execute('SELECT * FROM Items WHERE itemid = ?', itemId)
        item = cursor.fetchone()

        #if item is not none, then the item already exists!
        if item:
            cursor.execute('SELECT quantity FROM Items WHERE itemid = ?', itemId)
            oldQuantity = cursor.fetchone()
            cursor.execute('UPDATE Items SET itemname = ?, itemprice = ?, quantity = ? + ? WHERE itemid = ?', itemName, itemPrice, itemQuantity, oldQuantity, itemId)
            conn.commit()
        #itemId doesnt exist, do not update anything and send an error message!
        else:
            msg = 'Item does not exist!'

    #add print statement later!

    return render_template('', msg=msg)
    conn.close()

#Search items based on name or description -- choice will be either "name" or "description" ?
def searchItems(choice):
    msg = ''
    if requests.method == 'POST' and 'itemName' in requests.form and 'description' in requests.form:
        #Gets item information from form
        itemName = requests['itemName']
        itemDesc = requests['description']

        if choice == "description":
            #Add percent to front and end of string so it searches in any position
            likeDescrip = '%' + itemDesc + '%'
            cursor.execute('SELECT * FROM Items WHERE itemname LIKE ?', likeDescrip)
        else:
            #Add percent to front and end of string so it searches in any position
            likeDescrip = '%' + itemName + '%'
            cursor.execute('SELECT * FROM Items WHERE itemname LIKE ?', itemName)

        items = cursor.fetchall()

        # if there are items -> return to new database? Or return True but populate a new database and return false so frontend ppl can add html message or what not?
        if items:
            return render_template(''), items
        else
            msg = 'No results found!'
           
    return render_template('', msg=msg)
    conn.close()

# Order should be DESC or ASC ->Pass as var from html or as id, not sure yet
def sortByPrice(order):
    
    cursor.execute('SELECT * FROM Items ORDER BY itemprice ?', order)
    sortedItems = cursor.fetchall()

    return render_template(''), sortedItems
    conn.close()

#Order should be DESC or ASC -> Passed as a var by html? Not sure if that works
def sortByAvailability(order):
    if requests.method == 'POST' and 'itemId' in requests.form and 'itemQuantity' in requests.form:
    #Gets item information from form
        itemId = requests['itemId']
        itemQuantity = requests['itemQuantity']

        cursor.execute('SELECT * FROM Items ORDER BY quantity ?', order)
        sortedItems = cursor.fetchall()

        return render_template(''), sortedItems
        conn.close()