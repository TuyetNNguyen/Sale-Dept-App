import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import re

xl = pd.ExcelFile("SalesData.xlsx")
SalesData = xl.parse("Orders")
Decorating = "\n" + "*"*25 + "\n"
region_profit_columns = SalesData [["Region", "Sales"]]
SalesMonth = SalesData
SalesMonth["Year"] = SalesMonth["Order Date"].dt.year
sns.set(rc = {'figure.figsize' : (11,5)})

def Regional_Insight():

    Regional_Data_Input = input("Please enter the corresponding number to see the regional data: \n [1] Identify product sales by region each year \n [2] Identify total sales and total profit by region  \n [3] Go back to main menu \n \n ")
    
    while not Regional_Data_Input or not Regional_Data_Input.isdigit() or Regional_Data_Input.isdigit():
        if not Regional_Data_Input:
            Regional_Data_Input = input("Response cannot be blank. Please enter the corresponding number to see the regional data: \n [1] Identify product sales by region each year \n [2] Identify total sales and total profit by region \n [3] Go back to main menu \n \n ")
            continue
        
        if not Regional_Data_Input.isdigit():
            Regional_Data_Input= input("Response must contain numbers only. Please enter the corresponding number to see the regional data: \n [1] Identify product sales by region each year \n [2] Identify total sales and total profit by region \n [3] Go back to main menu \n \n ")
            continue
        
        if Regional_Data_Input.isdigit():
            Regional_Input_Int = int (Regional_Data_Input)
            if Regional_Input_Int == 0 or Regional_Input_Int > 3:
                Regional_Data_Input = input("Incorrect number. Please enter the corresponding number to see the regional data: \n [1] Identify product sales by region each year \n [2] Identify total sales and total profit by region \n [3] Go back to main menu \n \n ")
                continue
            if Regional_Input_Int == 1:
                
                Yearly_Sales_By_Quarter = SalesMonth[["Year", "Region", "Profit", "Sub-Category"]]
                Regional_Year = input("Please select the desired year to view: \n [1] 2014 \n [2] 2015 \n [3] 2016 \n [4] 2017 \n \n")
                while not Regional_Year or not Regional_Year.isdigit() or Regional_Year.isdigit():
                        if not  Regional_Year:
                            Regional_Year = input("Response cannot be blank. Please select the desired year to view: \n [1] 2014 \n [2] 2015 \n [3] 2016 \n [4] 2017 \n \n")
                            continue
                        if not  Regional_Year.isdigit():
                            Regional_Year= input("Response must contain numbers only. Please select the desired year to view: \n [1] 2014 \n [2] 2015 \n [3] 2016 \n [4] 2017 \n \n")
                            continue
                        if Regional_Year.isdigit():
                            Regional_Year_Input = int (Regional_Year)
                            
                            if Regional_Year_Input == 0 or Regional_Year_Input > 4:
                                Regional_Year = input("Incorrect number. Please select the desired year to view: \n [1] 2014 \n [2] 2015 \n [3] 2016 \n [4] 2017 \n \n")
                                continue
                            if Regional_Year_Input == 1:
            
                                year_sales = Yearly_Sales_By_Quarter.loc[Yearly_Sales_By_Quarter["Year"] == 2014]
                                region_profit_subCat = SalesData [["Region", "Profit", "Sub-Category"]]
                                regions = Yearly_Sales_By_Quarter.Region.unique()
                     #for each value in regions:
                                for region in regions:
                                 region_profit = region_profit_subCat.loc[region_profit_subCat["Region"] == region]
                                 region_total_profit = region_profit.groupby(by = "Sub-Category").sum().sort_values(by = "Profit", ascending = False)
                                 region_total_profit = region_total_profit.reset_index()
                                
                                 
                                 barchart1 = sns.barplot(x= "Sub-Category", y = "Profit", data = region_total_profit.head(10))
                                 barchart1.set_title("Top 10 Products in Terms of Profit \n Region: " + region + "\n Year: 2014")
                                 plt.rcParams.update({'font.size':8})
                                 plt.ylabel('Profit (Dollar Amount)')
                                 plt.show()
                            if Regional_Year_Input == 2:
            
                                year_sales = Yearly_Sales_By_Quarter.loc[Yearly_Sales_By_Quarter["Year"] == 2015]
                                region_profit_subCat = SalesData [["Region", "Profit", "Sub-Category"]]
                                regions = Yearly_Sales_By_Quarter.Region.unique()
                     #for each value in regions:
                                for region in regions:
                                 region_profit = region_profit_subCat.loc[region_profit_subCat["Region"] == region]
                                 region_total_profit = region_profit.groupby(by = "Sub-Category").sum().sort_values(by = "Profit", ascending = False)
                                 region_total_profit = region_total_profit.reset_index()
                                 barchart2 = sns.barplot(x= "Sub-Category", y = "Profit", data = region_total_profit.head(10))
                                 barchart2.set_title("Top 10 Products in Terms of Profit \n Region: " + region + "\n Year: 2015")
                                 plt.rcParams.update({'font.size':8})
                                 plt.ylabel('Profit (Dollar Amount)')
                                 plt.show()
                            if Regional_Year_Input == 3:
        
                                year_sales = Yearly_Sales_By_Quarter.loc[Yearly_Sales_By_Quarter["Year"] == 2016]
                                region_profit_subCat = SalesData [["Region", "Profit", "Sub-Category"]]
                                regions = Yearly_Sales_By_Quarter.Region.unique()
                     #for each value in regions:
                                for region in regions:
                                 region_profit = region_profit_subCat.loc[region_profit_subCat["Region"] == region]
                                 region_total_profit = region_profit.groupby(by = "Sub-Category").sum().sort_values(by = "Profit", ascending = False)
                                 region_total_profit = region_total_profit.reset_index()
                                 barchart3 = sns.barplot(x= "Sub-Category", y = "Profit", data = region_total_profit.head(10))
                                 barchart3.set_title("Top 10 Products in Terms of Profit \n Region: " + region + " \n Year: 2016")
                                 plt.rcParams.update({'font.size':8})
                                 plt.ylabel('Profit (Dollar Amount)')
                                 plt.show()
                            if Regional_Year_Input == 4:
        
                                year_sales = Yearly_Sales_By_Quarter.loc[Yearly_Sales_By_Quarter["Year"] == 2017]
                                region_profit_subCat = SalesData [["Region", "Profit", "Sub-Category"]]
                                regions = Yearly_Sales_By_Quarter.Region.unique()
                     #for each value in regions:
                                for region in regions:
                                 region_profit = region_profit_subCat.loc[region_profit_subCat["Region"] == region]
                                 region_total_profit = region_profit.groupby(by = "Sub-Category").sum().sort_values(by = "Profit", ascending = False)
                                 region_total_profit = region_total_profit.reset_index()
                                 barchart4 = sns.barplot(x= "Sub-Category", y = "Profit", data = region_total_profit.head(10))
                                 barchart4.set_title("Top 10 Products in Terms of Profit \n Region: " + region + " \n Year: 2017")
                                 plt.rcParams.update({'font.size':8})
                                 plt.ylabel('Profit (Dollar Amount)')
                                 plt.show()
                            break
                Regional_Data_Input = input("Insight Completed. Would you like to do something else?: \n [1] Identify product sales by region each year \n [2] Identify total sales and total profit by region \n [3] Go back to main menu \n \n ")
            if Regional_Input_Int == 2:  
                #Product Sales by Region with most profit
                 
                #find which region has the most sales
                
                region_profit_columns = SalesData [["Region", "Sales"]]
               
    
                region_total_sales = region_profit_columns.groupby(by = "Region").sum().sort_values(by = "Sales")
                region_total_sales = region_total_sales.reset_index()
                print("The following chart details each region based on their total sales: ")

                barchart5 = sns.barplot(x = "Region", y ="Sales", data = region_total_sales)
                barchart5.set_title("Total Sales by Region (2014-2017)")
                plt.ylabel('Sales (Dollar Amount)')
                plt.show()
                 
                  #find which region has the most profit
                region_profit_columns = SalesData [["Region", "Profit"]]
                region_total_profit = region_profit_columns.groupby(by = "Region").sum().sort_values(by = "Profit")
                region_total_profit = region_total_profit.reset_index()
                print("The following chart details each region based on their total profit: ")

                barchart6 = sns.barplot(x = "Region", y ="Profit", data = region_total_profit)
                barchart6.set_title("Total Profit by Region (2014-2017)")
                plt.ylabel('Profit (Dollar Amount)')
                plt.show()
                Regional_Data_Input = input("Insight Completed. Would you like to do something else?: \n [1] Identify product sales by region each year \n [2] Identify total sales and total profit by region \n [3] Go back to main menu \n \n ") 
               
            if Regional_Input_Int == 3:
             
                break
            
    
                
    
    
