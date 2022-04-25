import smtplib, ssl
import requests
import pyodbc 
import smtplib
import webbrowser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
from UserLogin import email



# creating nd viewing the html files in python


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=PAUL;'
                      'Database=Evergreen;'
                      'Trusted_Connection=yes;')


cursor = conn.cursor()


def cart():
    msg = ''
   #Gets item information from form
  
    if requests.methods == 'POST' and 'itemName' in requests.form and 'itemPrice' in requests.form and 'itemQuantity' in requests.form and 'discountCode' in requests.form and 'username' in requests.form and 'checkout' in requests.form and 'itemImage' in requests.form:
        itemName = requests['itemName']
        itemPrice = requests['itemPrice']
        itemQuantity = requests['itemQuantity']
        discountCode = requests['discountCode']
        username = requests['username']
        checkout = requests['Checkout']
        itemImage = requests['itemImage']
        orderDate = date.today()
        isEmpty =''
    
        isEmpty = cursor.execute('SELECT COUNT(*) AS RowCnt FROM Cart', isEmpty)
        conn.commit
    
   
   
   

   
        cursor.execute('SELECT * FROM Cart WHERE itemName = ?, amount = ?', itemName, itemQuantity)
        subtotal = cursor.execute('SELECT SUM(itemPrice*itemQuantity) FROM Cart', itemPrice, itemQuantity)
        cursor.execute('INSERT INTO Cart(subtotal) values(?)', subtotal)
        conn.commit()
   
        total = subtotal * (0.0825)
   
        cursor.execute('INSERT INTO Cart(total) values(?)', total)
        cursor.execute('INSERT INTO CurrentOrders(total) values(?)', total)
        conn.commit()

 
  
        if isEmpty==0:
            cursor.execute("INSERT INTO Cart SELECT * FROM CurrentOrders WHERE username = ?", username)
            conn.commit()
        if discountCode:
            cursor.execute('SELECT * FROM Discounts WHERE [Discount Code] = ?', discountCode)
            total = total - (total*discountCode)
            cursor.execute('INSERT INTO Cart(total) values(?)', total)
            cursor.execute('INSERT INTO CurrentOrders(total) values(?)', total)
            conn.commit()
        
        
        if checkout:
            cursor.execute('Insert Into PastOrders(itemName,itemPrice,itemQuantity, total, username, orderDate) values(?,?,?,?,?,?', 
                       itemPrice,itemQuantity, total, username, orderDate)
        
            cursor.execute('Delete From Cart')
            conn.commit()
            
            
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
            Thank you for puchasing from us!"""
            html = """\
            <html>
              <body>
                <p>Hi,<br>
                   Thank you for completing your order! Please click the link to see a copy of your receipt. 
                   Thank you!
                   
                   
                   
                   Click here toview receipt:<br>
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

        
    
conn.close()
    
    
        
        
    
    #add total to the Past and Current Orders DONE
    #clear cart when customer logs out DONE
    #use current order to pull the information back DONE
   #once checked out move to past orders DONE
   #need to implement date for orders DONE
   #calculae totals DONE
   #calculate discount codes DONE

    
    