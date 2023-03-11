
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import re
def SalesByQuarter():
    xl = pd.ExcelFile("SalesData.xlsx")
    SalesData = xl.parse("Orders")
   # Decorating = "\n" + "*"*25 + "\n"
    #Find which quarter had the most sales
    SalesMonth = SalesData
    SalesMonth["Quarter"] = SalesMonth["Order Date"].dt.quarter
    SalesMonth["Year"] = SalesMonth["Order Date"].dt.year
    quarter_sales_columns = SalesData [["Quarter", "Sales"]]
    sns.set(rc = {'figure.figsize' : (11,5)})
    
    
     
    Seasonal_Data_Input = input("Please enter the corresponding number to see the quarterly data: \n [1] Identify product sales by quarter each year \n [2] Identify total sales and total profit by quarter \n [3] Go back to main menu \n \n ")
    while not Seasonal_Data_Input or not Seasonal_Data_Input.isdigit() or Seasonal_Data_Input.isdigit():
        if not Seasonal_Data_Input:
            Seasonal_Data_Input = input("Response cannot be blank. Please enter a number from the given list: \n [1] Identify product sales by quarter each year \n [2] Identify total sales and total profit by quarter \n [3] Go back to main menu \n \n")
            continue
        if not Seasonal_Data_Input.isdigit():
            Seasonal_Data_Input= input("Response must contain numbers only. Please enter a number from the given list: \n [1] Identify product sales by quarter each year \n [2] Identify total sales and total profit by quarter \n [3] Go back to main menu \n \n")
            continue
        if Seasonal_Data_Input.isdigit():
            Input_Int = int (Seasonal_Data_Input)
            if Input_Int == 0 or Input_Int >=4:
                Seasonal_Data_Input = input("Incorrect number. Please enter a number from the given list: \n [1] Identify product sales by quarter each year \n [2] Identify total sales and total profit by quarter \n [3] Go back to main menu \n \n" )
                continue
            if Input_Int == 1:
                #find product sales by quarter
                    Yearly_Sales_By_Quarter = SalesMonth[["Year", "Quarter", "Sales", "Sub-Category"]]
                    Quarterly_Input = input("Please select the desired year to view: \n [1] 2014 \n [2] 2015 \n [3] 2016 \n [4] 2017 \n \n")
                    while not Quarterly_Input or not Quarterly_Input.isdigit() or Quarterly_Input.isdigit():
                        if not  Quarterly_Input:
                            Quarterly_Input = input("Response cannot be blank. Please select the desired year to view: \n [1] 2014 \n [2] 2015 \n [3] 2016 \n [4] 2017 \n \n")
                            continue
                        if not  Quarterly_Input.isdigit():
                            Quarterly_Input= input("Response must contain numbers only. Please select the desired year to view: \n [1] 2014 \n [2] 2015 \n [3] 2016 \n [4] 2017 \n \n")
                            continue
                        if Quarterly_Input.isdigit():
                            Quarterly_Input_Int = int (Quarterly_Input)
                            
                            if Quarterly_Input_Int == 0 or Quarterly_Input_Int > 4:
                                Quarterly_Input = input("Incorrect number. Please select the desired year to view: \n [1] 2014 \n [2] 2015 \n [3] 2016 \n [4] 2017 \n \n")
                                continue
                            if Quarterly_Input_Int == 1:
                                year_sales = Yearly_Sales_By_Quarter.loc[Yearly_Sales_By_Quarter["Year"] == 2014]
                                Quarter_sales_subCat = year_sales [["Quarter", "Sales", "Sub-Category"]]
                                Quarters = SalesData.Quarter.unique()
                                Quarters.sort()
                                for Quarter in Quarters:
                                    quarters_sales = Quarter_sales_subCat.loc[Quarter_sales_subCat["Quarter"] == Quarter]
                                    noquarters = quarters_sales [["Sales", "Sub-Category"]]
                                    quarter_total_sales = noquarters.groupby(by = "Sub-Category").sum().sort_values(by = "Sales", ascending = False)
                                    quarter_total_sales = quarter_total_sales.reset_index()
                                    barchart3 = sns.barplot(x= "Sub-Category", y = "Sales", data = quarter_total_sales.head(10))
                                    barchart3.set_title("Top 10 Products in Terms of Sales: Quarter " + str(Quarter) + " Year 2014")
                                    plt.rcParams.update({'font.size':3})
                                    plt.ylabel('Sales (Dollar Amount)')
                                    plt.show()
                                    
                            if Quarterly_Input_Int == 2:
                                year_sales = Yearly_Sales_By_Quarter.loc[Yearly_Sales_By_Quarter["Year"] == 2015]
                                Quarter_sales_subCat = year_sales [["Quarter", "Sales", "Sub-Category"]]
                                Quarters = SalesData.Quarter.unique()
                                Quarters.sort()
                                for Quarter in Quarters:
                                    quarters_sales = Quarter_sales_subCat.loc[Quarter_sales_subCat["Quarter"] == Quarter]
                                    noquarters = quarters_sales [["Sales", "Sub-Category"]]
                                    quarter_total_sales = noquarters.groupby(by = "Sub-Category").sum().sort_values(by = "Sales", ascending = False)
                                    quarter_total_sales = quarter_total_sales.reset_index()
                                    barchart4 = sns.barplot(x= "Sub-Category", y = "Sales", data = quarter_total_sales.head(10))
                                    barchart4.set_title("Top 10 Products in Terms of Sales: Quarter " + str(Quarter) + " Year 2015")
                                    plt.rcParams.update({'font.size':3})
                                    plt.ylabel('Sales (Dollar Amount)')
                                    plt.show()
                            if Quarterly_Input_Int == 3:
                                year_sales = Yearly_Sales_By_Quarter.loc[Yearly_Sales_By_Quarter["Year"] == 2016]
                                Quarter_sales_subCat = year_sales [["Quarter", "Sales", "Sub-Category"]]
                                Quarters = SalesData.Quarter.unique()
                                Quarters.sort()
                                for Quarter in Quarters:
                                    quarters_sales = Quarter_sales_subCat.loc[Quarter_sales_subCat["Quarter"] == Quarter]
                                    noquarters = quarters_sales [["Sales", "Sub-Category"]]
                                    quarter_total_sales = noquarters.groupby(by = "Sub-Category").sum().sort_values(by = "Sales", ascending = False)
                                    quarter_total_sales = quarter_total_sales.reset_index()
                                    barchart5 = sns.barplot(x= "Sub-Category", y = "Sales", data = quarter_total_sales.head(10))
                                    barchart5.set_title("Top 10 Products in Terms of Sales: Quarter " + str(Quarter) + " Year 2016")
                                    plt.rcParams.update({'font.size':3})
                                    plt.ylabel('Sales (Dollar Amount)')
                                    plt.show()
                            if Quarterly_Input_Int == 4:
                                year_sales = Yearly_Sales_By_Quarter.loc[Yearly_Sales_By_Quarter["Year"] == 2017]
                                Quarter_sales_subCat = year_sales [["Quarter", "Sales", "Sub-Category"]]
                                Quarters = SalesData.Quarter.unique()
                                Quarters.sort()
                                for Quarter in Quarters:
                                    quarters_sales = Quarter_sales_subCat.loc[Quarter_sales_subCat["Quarter"] == Quarter]
                                    noquarters = quarters_sales [["Sales", "Sub-Category"]]
                                    quarter_total_sales = noquarters.groupby(by = "Sub-Category").sum().sort_values(by = "Sales", ascending = False)
                                    quarter_total_sales = quarter_total_sales.reset_index()
                                    barchart6 = sns.barplot(x= "Sub-Category", y = "Sales", data = quarter_total_sales.head(10))
                                    barchart6.set_title("Top 10 Products in Terms of Sales: Quarter " + str(Quarter) + " Year 2017")
                                    plt.rcParams.update({'font.size':3})
                                    plt.ylabel('Sales (Dollar Amount)')
                                    plt.show()
                            
                            break
                    Seasonal_Data_Input = input("Insight Completed. Would you like to do something else?: \n [1] Identify product sales by quarter each year \n [2] Identify total sales and total profit by quarter \n [3] Go back to main menu \n \n") 
    
            if Input_Int == 2:
                quarter_total_sales = quarter_sales_columns.groupby(by = "Quarter").sum().sort_values(by = "Sales")
                quarter_total_sales = quarter_total_sales.reset_index()
                print("The following chart details each quarter based on their total sales: ")
    
                #prints bar graph
                barchart1 = sns.barplot(x= "Quarter", y = "Sales", data = quarter_total_sales)
                barchart1.set_title("Total Sales by Quarter (2014-2017)")
                plt.ylabel('Sales (Dollar Amount)')
                plt.show()
        
                QuarterProfit = SalesMonth[["Quarter" ,"Profit"]]
                quarter_total_profit = QuarterProfit.groupby(by = "Quarter").sum().sort_values(by = "Profit")
                print("\n The following chart details each quarter based on their total profit: ")
              
                quarter_total_profit = quarter_total_profit.reset_index()
                barchart2 = sns.barplot(x = "Quarter", y = "Profit", data = quarter_total_profit)
                barchart2.set_title("Total Profit by Quarter (2014-2017)")
                plt.ylabel('Profit (Dollar Amount)')
                plt.show()
                
                Seasonal_Data_Input = input("Insight Completed. Would you like to do something else?: \n [1] Identify product sales by quarter each year \n [2] Identify total sales and total profit by quarter \n [3] Go back to main menu \n \n") 
    
            
            if Input_Int == 3:
                break
