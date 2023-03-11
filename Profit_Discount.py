import pandas as pd
xl = pd.ExcelFile("SalesData.xlsx")
SalesDatae = xl.parse("Orders")
import pandas as pd
xl = pd.ExcelFile("SalesData.xlsx")
SalesData = xl.parse("Orders")
 
def profit_SubMenu ():
    Decorating = "\n" + "*"*45 + "\n"
    print("Sumarization of the profit, sales, and discount that sold in the past 4 years: ")
    SalesYear = SalesData
    SalesYear["Year"] = SalesYear["Order Date"].dt.year
    YearlySales = SalesYear [["Year", "Sales", "Profit"]]
    YearlyTotalSales = YearlySales.groupby(by= "Year").sum()
    YearlyTotalSales = YearlyTotalSales.reset_index()
    print(YearlyTotalSales)
    print(Decorating)
   
    required_input = 1
    while required_input == 1:
        profit_SubMenu = input ("Please select a number from 1 to 3 below: \n [1] The top 5 profitable products and its sale data \n [2] The least 5 profitable products and its sale data \n [3] Main menu \n Please enter here: ")
        if not profit_SubMenu:
            profit_SubMenu = input("Input value cannot be blank or space. Please re-enter a number from 1 to 4: ")
            continue
        if not profit_SubMenu.isdigit():
            profit_SubMenu = input ("Input must be numerical value. Please re-enter a number from 1 to 4: ")
            continue
        profit_SubMenu = int(profit_SubMenu)
        if not profit_SubMenu > 0:
            profit_SubMenu = input("Input value cannot be equal or less than 0. Please re-enter a number 1 to 4: ")
            continue
        if not profit_SubMenu <= 4:
            profit_SubMenu = input("Input value cannot be greater than 4. Please re-enter a number from 1 to 4: ")
            continue
   
        if profit_SubMenu == 1:
 
                print("------------------------------------------------")
                print("TOP PROFITABLE PRODUCTS AND ITS SALE DATA")
                year_profit_discount = SalesData [["Profit", "Sales","Product Name","Year"]]
                years = SalesData.Year.unique()
                years.sort()
                #year_profit = year_profit_discount.loc[year_profit_discount["Discount"] !=  0]
               
                required_input_sub = 1
                while required_input_sub == 1:
                    profit_discount = input ("Please enter a number from 1 to 4 to see detail data: \n [1] The top 5 profitable products that sold the most \n [2] The top 5 profitable products that sold the least \n [3] Main menu \n [4] Go back \n Please enter here: ")
                   
                    if profit_discount == "1":
                        for SalesYear in years:
                            year_profit = year_profit_discount.loc[year_profit_discount["Year"] == SalesYear]
                            year_total_profit = year_profit.groupby(by = ["Product Name","Year"]).sum().sort_values(by = "Profit").sort_values(by = "Sales", ascending = False )
                            print("The top 5 profitable products that sold the most in " + str(SalesYear) + " are: ")
                            year_total_profit = year_total_profit.reset_index()
                            print(year_total_profit.head(5))
                            print(Decorating)
                           
                    if profit_discount == "2":
                        for SalesYear in years:
                            year_profit = year_profit_discount.loc[year_profit_discount["Year"] == SalesYear]
                            year_total_profit = year_profit.groupby(by = ["Product Name", "Year"]).sum().sort_values(by = ["Profit", "Sales"], ascending = False)
                            print("The top 5 profitable products that sold the least in " + str(SalesYear) + " are: ")
                            year_total_profit = year_total_profit.reset_index()
                            print(year_total_profit.head(5))
                            print(Decorating)
                           
                    if profit_discount == "3":
                        required_input_sub = 0
 
                        profit_SubMenu = 3
                        break
                    if profit_discount == "4":
                        required_input_sub = 0
                        break
           
        if profit_SubMenu ==2:
           
                print("-------------------------------------------")
                print("LEAST PROFITABLE PRODUCTS AND ITS SALE DATA")
                year_profit_wdiscount = SalesData [["Year", "Product Name", "Profit", "Sales"]]
                years = SalesData.Year.unique()
                years.sort()
                #year_profit = year_profit_wdiscount.loc[year_profit_wdiscount["Discount"] ==  0]
               
                required_input_sub = 1
                while required_input_sub == 1:
                    profit_noDiscount = input ("Please enter a number from 1 to 4 to see detail data: \n [1] The least 5 profitable products that sold the most \n [2] The least 5 profitable products that sold the least \n [3] Main menu \n [4] Go back \n Please enter here: ")
                   
                    if profit_noDiscount == "1":
                        for SalesYear in years:
                            year_profit = year_profit_wdiscount.loc[year_profit_wdiscount["Year"] == SalesYear]
                            year_total_profit = year_profit.groupby(by = ["Product Name", "Year"]).sum().sort_values(by = ["Profit", "Sales"], ascending = False)
                            print("The least 5 profitable products that sold the most in " + str(SalesYear) + " are: ")
                            year_total_profit = year_total_profit.reset_index()
                            print(year_total_profit.tail(5))
                            print(Decorating)
                           
                    if profit_noDiscount == "2":      
                        for SalesYear in years:
                            year_profit = year_profit_wdiscount.loc[year_profit_wdiscount["Year"] == SalesYear]
                            year_total_profit = year_profit.groupby(by = ["Product Name", "Year"]).sum().sort_values(by = "Profit").sort_values(by = "Sales", ascending = False)
                            print("The least 5 profitable products that sold the least in " + str(SalesYear) + " are: ")
                            year_total_profit = year_total_profit.reset_index()
                            print(year_total_profit.tail(5))
                            print(Decorating)
                           
                    if profit_noDiscount == "3":
                        required_input_sub = 0
 
                        profit_SubMenu = 3
                        break
                    if profit_noDiscount == "4":
                        required_input_sub = 0
                        break
           
        if profit_SubMenu == 3:
       
            break

