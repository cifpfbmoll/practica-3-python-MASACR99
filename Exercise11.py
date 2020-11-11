day,month,year = input("Put day, month and year separated by a space: ").split()
day = int(day)
month = int(month)
year = int(year)
full_days_months = [1,3,5,7,8,10,12]
not_full_days_months = [4,6,9,11]
if month in full_days_months:
    if day <= 31 and day >= 0:
        print(str(day)+"/"+str(month)+"/"+str(year)+"->Valid date")
    else:
        print(str(day)+"/"+str(month)+"/"+str(year)+"->Not a valid date")
elif month in not_full_days_months:
    if day <= 30 and day >= 0:
        print(str(day)+"/"+str(month)+"/"+str(year)+"->Valid date")
    else:
        print(str(day)+"/"+str(month)+"/"+str(year)+"->Not a valid date")
elif month == 2:
    if (year % 4) == 0:  
        if (year % 100) == 0:  
            if (year % 400) == 0:  
                if day <= 29 and day >= 0:
                    print(str(day)+"/"+str(month)+"/"+str(year)+"->Valid date")
                else:
                    print(str(day)+"/"+str(month)+"/"+str(year)+"->Not a valid date")
            else:
                if day <= 28 and day >= 0:
                    print(str(day)+"/"+str(month)+"/"+str(year)+"->Valid date")
                else:
                    print(str(day)+"/"+str(month)+"/"+str(year)+"->Not a valid date")
        else:  
            if day <= 29 and day >= 0:
                print(str(day)+"/"+str(month)+"/"+str(year)+"->Valid date")
            else:
                print(str(day)+"/"+str(month)+"/"+str(year)+"->Not a valid date")
    else:
        if day <= 28 and day >= 0:
            print(str(day)+"/"+str(month)+"/"+str(year)+"->Valid date")
        else:
            print(str(day)+"/"+str(month)+"/"+str(year)+"->Not a valid date")
else:
    print(str(day)+"/"+str(month)+"/"+str(year)+"->Not a valid date")