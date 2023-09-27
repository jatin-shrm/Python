#Calculator with function
def calculator(first,opt,second):
    if opt=="+":
        return first+second
    elif opt=="-":
        return first-second
    elif opt=="*":
        return first*second
    elif opt=="/":
        return first/second

def calculate():
    first_number=float(input("What's your number: "))
    calculation=False
    while not calculation:
        
        operation=input("What's your operation: ")
        next_number=float(input("What's your next number: "))
        ans=calculator(first_number,operation,next_number)
        print(ans)
        new_cal=input("Type \"y\" to continue with 2.5 , or type \"n\" to start a new calculation:  ").lower()
        if new_cal=="y":
            first_number=ans
        else:
            calculation=True
            calculate()
calculate()