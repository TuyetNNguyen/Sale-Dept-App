import sqlite3
import re


conn = sqlite3.connect("OS_Employee.db")

def login():
   print("Welcome to Office Solution")
   print("-----------------------------------------------")
   print("Employee Login")
   print("-----------------------------------------------")
   email = "@gmail.com"
   userEmail = input("Please enter your email to login in: ")
   #checks if user inputs a blank email
   while not userEmail:
        userEmail = input("Email cannot be blank. Please enter your email to login in: ")
        
   #checks if user inputs a domain for email 
   while not email in userEmail:
       userEmail = input("The following includes an invalid domain, please try again: ")
       if not userEmail:
           userEmail = input("Email cannot be blank. Please enter your email to login in: ")
           continue
   userPassword = input("Please enter your password: ")
   #checks if user inputs a blank password
   while not userPassword:
        userPassword = input("Password cannot be blank. Please enter your password to login: ")
   with conn:
        cur = conn.cursor()
        try:
            cur.execute("SELECT COUNT (*) FROM Employee WHERE(Email = '" + userEmail +"' AND Password = '" + userPassword + "') ")
            results = cur.fetchone()
            if results[0]==1:
                print("Login successful!")
            else:
                print("Login Unsuccessful. Information does not match database. Please try again. \n") 
                login()
        except:
                print ("Connection to database was lost. Please run the application again.")
