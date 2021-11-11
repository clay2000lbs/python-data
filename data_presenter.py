# Create a new file called data_presenter.py.

# Open the CupcakeInvoices.csv.
invoice = open("cupcakeInvoices.csv")

# Loop through all the data and print each row.
# for order in invoice:
#     print(order)

# Loop through all the data and print the type of cupcakes purchased.
# cupcakes = []
# def findCupcake():
#     for order in invoice:
#         print(order.split(",")[2])
        
# findCupcake()        
    

# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
def findSubTotal():
    for order in invoice:
        quant = order.split(",")[3]
        quantFloat = float(quant)
        #print(quantFloat)
        price = order.split(",")[4]
        priceFloat = float(price)
        #print(priceFloat)
        subtotal = quantFloat * priceFloat
        print(round(subtotal,2))

#findSubTotal()

# Loop through all the data, and print out the total for all invoices combined.
def findTotal():
    total = []
    for order in invoice:
        quant = order.split(",")[3]
        quantFloat = float(quant)
        #print(quantFloat)
        price = order.split(",")[4]
        priceFloat = float(price)
        #print(priceFloat)
        subtotal = round((quantFloat * priceFloat), 2)
        total.append(subtotal)
    print(round(sum(total), 2))    
    #print(total)

        
findTotal()
# Close your open file.


