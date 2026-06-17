# importing all libraries
import pyfiglet
import time
import colorama
from openpyxl import Workbook

# Creating a dictonary with stocks and there prices
stocks={"Hdfc":772.45,"Bharati":1822.50,"Reliance":1293,"Icici":
        1340,"Sbi":1017.15,"Tata":2161,"Larsen":4049.30,"Apple":
        27706.84,"Tesla":38679.94,"Google":34230.75,"Microsoft":37186.73}


# Creating an empty dictionary to store data of individual
personalStocks={}

# Iterating loop to get input from user
while True:


    # Basic user interface
    print("""   ====================================
        📊 STOCK PORTFOLIO TRACKER
   ====================================

    [1] Add Stock
    [2] View Portfolio
    [3] Total Value
    [4] Save Report
    [5] Exit

    ------------------------------------
    """)

    # Taking input from user
    choice=int(input("> Enter your choice: "))


    # Working on user input
    if(choice==1):
        stock=input(">Enter stock starting name :: ").capitalize()
        if stock in stocks:
            quantity=int(input(">Enter the quantity of stocks :: "))
            personalStocks[stock]=quantity
            print("✅ Stock added successfully .")
            # print(personalStocks)
        else:
            print("🚨 Add valid stock .")
        print("\n")

    # User can view his entire data here 
    elif(choice==2):
        print("Stock"    "  ||  "    "Qty"    "  ||  "    "Price"    "  ||  "    "Total")
        for stock in personalStocks:
            print(stock," || ",personalStocks[stock],
                  " || ",(stocks[stock])," || ",personalStocks[stock]*stocks[stock])
        print("\n")


    # User can see entire investment here 
    elif(choice==3):
        total=0
        for stock in personalStocks:
            total+=stocks[stock]*personalStocks[stock]
        print("\033[94m 🟢 Total Investment is ::\033[0m",total)
        print("\n")


    # Saving report 
    elif(choice==4):
        ch=input("Do you want to save report ?[Y/N] :: ")
        if(ch=='Y' or ch=='y'):
            wb = Workbook()
            ws=wb.active
            ws.append(["Stock","QTY","Price","Total"])
            for stock in personalStocks:
                ws.append([stock,personalStocks[stock],
                           stocks[stock],personalStocks[stock]*stocks[stock]])
            wb.save("portfolio.xlsx")
            print("✅ Data saved successfully !!")
        print("\n")


    # Exiting 
    elif(choice==5):
        break

    # Handling invalid inputs 
    else:
        print("Enter valid choice !!")