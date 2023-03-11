import sqlite3

from Login_Final import login
from Main_Menu import Main_Menu

conn = sqlite3.connect("OS_Employee.db")


login()   
Main_Menu()        
