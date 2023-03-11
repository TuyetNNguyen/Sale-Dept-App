from SalesByQuarter import SalesByQuarter
from CustomerLoyalty import CustomerLoyaltyMenu
from RegistrationTest import Registration
from Profit_Discount import profit_SubMenu
from Region_Profit import Regional_Insight
from Update import Update_Info

def Main_Menu():
   
    Main_Menu_input = input("Welcome, please input the number corresponding to the task you would like to perform: \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View top 20% of customers for loyalty program \n [5] Register new user \n [6] Update employee information \n [7] Logout \n \n")
    
    while not Main_Menu_input or not Main_Menu_input.isdigit() or Main_Menu_input.isdigit():
        if not Main_Menu_input:
            Main_Menu_input = input("Response cannot be blank. Please input the number corresponding to the task you would like to perform: \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View top 20% of customers for loyalty program \n [5] Register new user \n [6] Update employee information \n [7] Logout \n \n")
            continue
        if not Main_Menu_input.isdigit():
            Main_Menu_input= input("Response must contain numbers only. Please input the number corresponding to the task you would like to perform: \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View top 20% of customers for loyalty program \n [5] Register new user \n [6] Update employee information \n [7] Logout \n \n")
            continue
        if Main_Menu_input.isdigit():
            Main_Menu_input_int = int(Main_Menu_input)
            
            if Main_Menu_input_int <= 0 or Main_Menu_input_int >=8:
                
                Main_Menu_input= input("Incorrect number. Please input the number corresponding to the task you would like to perform: \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View top 20% of customers for loyalty program \n [5] Register new user \n [6] Update employee information \n [7] Logout \n \n")

                
            if Main_Menu_input_int == 1:
                
                SalesByQuarter()
                
                Main_Menu_input = input("Welcome, please input the number corresponding to the task you would like to perform: \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View top 20% of customers for loyalty program \n [5] Register new user \n [6] Update employee information \n [7] Logout \n \n")
           
            if Main_Menu_input_int == 2:
                
                Regional_Insight()
                
                Main_Menu_input = input("Welcome, please input the number corresponding to the task you would like to perform: \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View top 20% of customers for loyalty program \n [5] Register new user \n [6] Update employee information \n [7] Logout \n \n")

            
            if Main_Menu_input_int == 3:
                
                profit_SubMenu()
                
                Main_Menu_input = input("Welcome, please input the number corresponding to the task you would like to perform: \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View top 20% of customers for loyalty program \n [5] Register new user \n [6] Update employee information \n [7] Logout \n \n")

            
            if Main_Menu_input_int == 4:
               
                CustomerLoyaltyMenu()
                
                Main_Menu_input = input("Welcome, please input the number corresponding to the task you would like to perform: \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View top 20% of customers for loyalty program \n [5] Register new user \n [6] Update employee information \n [7] Logout \n \n")

            if Main_Menu_input_int == 5:
                
                Registration()
                
                Response_input = input("Would you like to register a new user or quit? \n [1] Yes \n [2] No \n \n")
                Response_input_int = int(Response_input)
                
                if Response_input_int == 1:
                    Main_Menu_input_int = 5
                
                if Response_input_int == 2:
                    Main_Menu_input = input("Welcome, please input the number corresponding to the task you would like to perform: \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View top 20% of customers for loyalty program \n [5] Register new user \n [6] Update employee information \n [7] Logout \n \n")
                
                if Response_input_int != 1 and Response_input_int != 2:
                    Response_input = input("Incorrect input. Would you like to register a new user or quit? \n [1] Yes \n [2] No \n \n")
                
            if Main_Menu_input_int == 6:
                
                Update_Info()
                
                Update_Info_input = input("Would you like to update another user or quit? \n [1] Yes \n [2] No \n \n")
                Update_Info_input_int = int(Update_Info_input)
                
                if Update_Info_input_int == 1:
                    Main_Menu_input_int = 6
                
                if Update_Info_input_int == 2:
                    Main_Menu_input = input("Welcome, please input the number corresponding to the task you would like to perform: \n [1] View Quarterly Sales Data Information \n [2] View Regional Sales Data Information \n [3] View Yearly Profit and Sales \n [4] View top 20% of customers for loyalty program \n [5] Register new user \n [6] Update employee information \n [7] Logout \n \n")
                
                if Update_Info_input_int != 1 and Update_Info_input_int != 2:
                    Update_Info_input = input("Incorrect input. Would you like to register a new user or quit? \n [1] Yes \n [2] No \n \n")

            if Main_Menu_input_int == 7:
                print("Thank you for using Office Solutions. We hope to see you again soon!")
                break
                
                
