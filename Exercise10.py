prod_name = input("Enter the name of the product")
price = float(input("Enter price of product"))
IVA = 21
print("Your " + prod_name + " costs " + str(price) + " euros and with " + str(IVA) + " % it totals: " + str(price+price*IVA/100))