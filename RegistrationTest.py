import sqlite3
import re
conn = sqlite3.connect("OS_Employee.db")
 
def checkUniqueEmployId(EmpID) :
    with conn:
        cur = conn.cursor()
        try:
            cur.execute("SELECT count(*) FROM Employee WHERE(EmployeeID == '{}')".format(EmpID))
            results = cur.fetchone()
    # Error checking 1: Tell user that the employee ID entered already exists.
            if results[0]==1:  
                return False
            return True
        except Exception as e:
            print("Connection to database was lost. Please run the application again." + str(e))
def checkUniqueEmail(email) :
    with conn:
        cur = conn.cursor()
        try:
            cur.execute("SELECT count(*) FROM Employee WHERE(Email == '{}')".format(email))
            results = cur.fetchone()
    # Error checking 1: Tell user that the Email entered already exists.
            if results[0]==1:  
                return False
            return True
        except Exception as e:
            print("Connection to database was lost. Please run the application again." + str(e))
       
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
 
def Registration():
           
            print("--------------------------------------------")
            print("Register a New User")
           
        #EmployeeID():
            EmpID = input("Please enter your employee ID number: ")
             # Error checking 1: employee ID must not be blank.
            while not checkUniqueEmployId(EmpID) or not EmpID or not EmpID.isdigit() or not len(EmpID) == 4:
                if not checkUniqueEmployId(EmpID):
                    EmpID = input("Employee ID already taken, please try again: ")
                    continue
                if not EmpID:
                    EmpID = input("ID cannot be blank, please try again: ")
                    continue
                # Error checking 2: employee ID must be in numerical values only.
                if not EmpID.isdigit():
                    EmpID = input("Employee ID must contain numbers only. Please try again: ")
                    continue
                # Error checking 3: employee ID must be 4 digits long
                if not len(EmpID) == 4:
                    if len(EmpID) < 4:
                        EmpID = input("Incorrect number of digits, please try again: ")
                    if len(EmpID) > 4:
                        EmpID = input("Incorrect number of digits, please try again: ")
                    continue
        #First Name():          
            space = " "        
            F_Name = input("Please enter first name: ")
            F_Name.lower()
            while not F_Name or not F_Name.isalpha() or not F_Name[0].isupper():
                #checks for blank spaces
                if not F_Name:
                    F_Name = input ("First name cannot be blank. Please re-enter your first name: ").lower()
                   
                    continue
                #checks for unnecessary space.
                if not F_Name.isalpha():
                    if space in F_Name:
                        F_Name = input("The following contains an unnecessary space. Please try again: ").lower()
                     
                 #checks for characters that are not an alphabet.      
                    else:
                        F_Name = input("The following contains characters not in the traditional alphabet. Please try again: ").lower()
                       
                    continue
                if not F_Name[0].isupper():
                    F_Name = F_Name.capitalize()
                    print(F_Name)
                    continue
        #Last Name():          
            L_Name = input("Please enter last name: ")
            L_Name.lower()
            while not L_Name or not L_Name.isalpha() or not L_Name[0].isupper():
                #checks for blank spaces
                if not L_Name:
                    L_Name = input ("Last name cannot be blank. Please re-enter your last name").lower()
                   
                    continue
                #checks for unnecessary space.
                if not L_Name.isalpha():
                    if space in L_Name:
                        L_Name = input("The following contains an unnecessary space. Please try again: ").lower()
                     
                 #checks for characters that are not an alphabet.    
                    else:
                        L_Name = input("The following contains characters not in the traditional alphabet. Please try again: ").lower()
                       
                    continue
                if not L_Name[0].isupper():
                    L_Name = L_Name.capitalize()
                    print(L_Name)
                    continue
               
        #Email():    
            email = "@gmail.com"    
            userEmail = input("Please enter email: ")
            while not userEmail or not email in userEmail:
              #checks if user input is blank
               if not userEmail:
                    userEmail = input("Email cannot be blank. Please enter your email to login in: ")
                    continue
                   
               #checks if user inputs a domain for email
               if not email in userEmail:
                   userEmail = input("The following includes an invalid domain, please try again: ")
                   continue
               
               if not checkUniqueEmail(userEmail):
                   userEmail = input("Email is already taken, please try again: ")
                   continue
               valid = True;
         
        #Password ():    
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            Password = input("Please enter your new password. The password should have greater than 8 characters and at least one  number, one capital letter, and a special character: ")
            while not Password or len(Password) < 8 or Password.isalpha() or not hasNumbers(Password) or regex.search(Password) == None:
                if not Password: #checks if password is blank
                    Password = input ("Password cannot be blank. Please re-enter an adjusted password: ")
                    continue
                if len(Password) < 8: #checks if password is less than 8 chracters long
                    Password = input ("Password is not of correct length. Please re-enter an adjusted password: ")
                    continue
                if not hasNumbers(Password): #checks if password contains at least one number
                    Password = input("Password does not contain any numbers. Please re-enter an adjusted password: ")
                    continue
                if(regex.search(Password) == None): #checks if password contains at least one special character
                    Password = input("Password does not contain any special characters. Please re-enter an adjusted password: ")
                    continue
                   
        #Password Confirmation
            Password1 = input("Please verify your new password: ")
            while (Password != Password1):
                Password1= input("Passwords do not match. Please try again: ")    
           
            print("Registration Complete! All fields were inputted correctly")
         
            with conn:
                cur = conn.cursor()
                try:
                     InsertValue = "INSERT INTO Employee VALUES ('{}','{}','{}','{}','{}')"
                     InsertString = InsertValue.format(EmpID,F_Name,L_Name,userEmail,Password)
                     cur.execute(InsertString)
                     cur.execute("SELECT*FROM Employee WHERE(EmployeeID == '{}')".format(EmpID))
         #order of argument matters, does not know the difference between last name or employeeID.
                     results = cur.fetchone()
                     print(results)
                except Exception as e:
                    print("Connection to database was lost. Please run the application again." + str(e))

