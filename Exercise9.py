number = int(input("Enter a number with 3 numbers or less"))
if number >= 999 or number <= -999:
    print("Error: " + str(number) + " has more than 3 numbers")