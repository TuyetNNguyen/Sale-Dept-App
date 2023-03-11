import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
xl = pd.ExcelFile("SalesData.xlsx")
SalesData = xl.parse("Orders")
Decorating = "\n" + "*"*25 + "\n"
 
def CustomerLoyaltyMenu():
    #Main Menu for Customer Loyalty Program
    customer_loyalty = input("Please enter a number from 1-4 to look at the data insights for customer loyalty program: \n [1] Customer Segment Purchase Frequency \n [2] Top 10 Customers By Segment With/Without Discount \n [3] Bottom 10 Customers By Segment With/Without Discount \n [4] Go Back To Main Menu \n \n ")
    while not customer_loyalty or not customer_loyalty.isdigit() or customer_loyalty.isdigit():
        if not customer_loyalty:
            customer_loyalty = input("Response cannot be blank. Please re-enter a number from 1-4 to look at the data insights for customer loyalty program:  \n [1] Customer Segment Purchase Frequency \n [2] Top 10 Customers By Segment With/Without Discount \n [3] Bottom 10 Customers By Segment With/Without Discount \n [4] Go Back To Main Menu \n \n")
            continue
        if not customer_loyalty.isdigit():
            customer_loyalty = input("You must enter a numerical value. Please re-enter a number from 1-4 to look at the data insights for customer loyalty program: \n [1] Customer Segment Purchase Frequency \n [2] Top 10 Customers By Segment With/Without Discount \n [3] Bottom 10 Customers By Segment With/Without Discount \n [4] Go Back To Main Menu \n \n")
            continue
        if customer_loyalty.isdigit():
            Enter_Int = int(customer_loyalty)
            if Enter_Int == 0 or Enter_Int > 4:
                customer_loyalty = input("Incorrect number. Please enter a number from 1-5: \n [1] Customer Segment Purchase Frequency \n [2] Top 10 Customers By Segment With/Without Discount \n [3] Bottom 10 Customers By Segment With/Without Discount \n [4] Go Back To Main Menu \n \n" )
                continue
            
            #CUSTOMER SEGMENT PURCHASE FREQUENCY
            if Enter_Int == 1:
                MostFrequent = SalesData["Segment"].value_counts()
                MostFrequent = MostFrequent.reset_index()
                MostFrequentrename = MostFrequent.rename(columns = {"index": "Segment", "Segment" : "Frequency"})
                sns.set(rc={'figure.figsize': (9,7)})
                barchart1 = sns.barplot(x = "Segment", y = "Frequency", data = MostFrequentrename)
                barchart1.set_title("Customer Segment Purchase Frequency")
                plt.show()
    
 
          
            #TOP 10 CUSTOMERS BY SEGMENTS WITH DISCOUNTS  
            if Enter_Int == 2:
                segment_discount_Cus = SalesData [["Segment", "Discount", "Customer Name", "Profit"]]
                Segments = SalesData.Segment.unique() 
                for Segment in Segments:
                    segment_discount = segment_discount_Cus.loc[segment_discount_Cus["Segment"] == Segment]
                    segment_total_discount = segment_discount.groupby(by = "Customer Name").sum().sort_values(by = "Discount" and "Profit", ascending = False)
                    segment_total_discount = segment_total_discount.reset_index()
                    print("The top 10 Customers purchasing with Discount in  " + Segment + " are: ")
                    print(segment_total_discount.head(10))
                    print(Decorating)
                    
            #TOP 10 CUSTOMERS BY SEGMENTS WITHOUT DISCOUNTS
                segment_no_Cus = SalesData [["Segment", "Discount", "Customer Name", "Profit"]]
                segment_no_Cus_no_discount = segment_no_Cus.loc[segment_no_Cus["Discount"] == 0]
                Segments = SalesData.Segment.unique() 
                for Segment in Segments:
                    segment_no =segment_no_Cus_no_discount.loc[segment_no_Cus_no_discount["Segment"] == Segment]
                    segment_total_no = segment_no.groupby(by = "Customer Name").sum().sort_values(by = "Profit", ascending = False)
                    segment_total_no = segment_total_no.reset_index()
                    print("The top 10 Customers purchasing without discount in " + Segment + " are: ")
                    print(segment_total_no.head(10))
                    print(Decorating)
                    
            #BOTTOM 10 CUSTOMERS BY SEGMENTS WITH DISCOUNT
            if Enter_Int == 3:
                segment_discount_Cus = SalesData [["Segment", "Discount", "Customer Name", "Profit"]]
                Segments = SalesData.Segment.unique() 
                
                for Segment in Segments:
                    segment_discount = segment_discount_Cus.loc[segment_discount_Cus["Segment"] == Segment]
                    segment_total_discount = segment_discount.groupby(by = "Customer Name").sum().sort_values(by = "Discount" and "Profit", ascending = False)
                    segment_total_discount = segment_total_discount.reset_index()
                    print("The bottom 10 Customers purchasing with Discount in  " + Segment + " are: ")
                    print(segment_total_discount.tail(10))
                    print(Decorating)
                    
            #BOTTOM 10 CUSTOMERS BY SEGMENTS WITHOUT DISCOUNTS
                segment_no_Cus = SalesData [["Segment", "Discount", "Customer Name", "Profit"]]
                segment_no_Cus_no_discount = segment_no_Cus.loc[segment_no_Cus["Discount"] == 0]
                
                Segments = SalesData.Segment.unique() 
                for Segment in Segments:
                    segment_no =segment_no_Cus_no_discount.loc[segment_no_Cus_no_discount["Segment"] == Segment]
                    segment_total_no = segment_no.groupby(by = "Customer Name").sum().sort_values(by = "Profit", ascending = False)
                    segment_total_no = segment_total_no.reset_index()
                    print("The bottom 10 Customers purchasing without discount in " + Segment + " are: ")
                    print(segment_total_no.tail(10))
                    print(Decorating)
                    
            if Enter_Int == 4:
                print("Insert Main Menu")
            
            customer_loyalty = input("Insight Completed. Would you like to do something else?: \n [1] Customer Segment Purchase Frequency \n [2] Top 10 Customers By Segment With/Without Discount \n [3] Bottom 10 Customers By Segment With/Without Discount \n [4] Go Back To Main Menu \n \n")
 



