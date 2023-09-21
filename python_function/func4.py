#Bill spliter
#tip 10,12,15 %
print("Welcome to the bill calculator")
total_bill=float(input("What was the total bill: "))
no_of_people=int(input("How many people to split the bill: "))
tip=int(input("What percentage you want to give tip: "))
total_tip=(total_bill*tip)/100
bill_after_tip=total_bill+total_tip
split_money=round(bill_after_tip/no_of_people,2)
print(f"Each person should pay {split_money} Rupess")