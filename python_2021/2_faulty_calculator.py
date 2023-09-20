#Faulty Calculator
#45*3=555 56+9=77 56/6=4 , these are wrong values
n1=input("Enter the operator\n",)
n2=int(input("Enter the first number\n",))
n3=int(input("Enter the second number\n",))
if n1=="*":
    if n2==45 and n3==3:
        print(555)
    elif n2==45 and n3==3:
        print(555)
    else:
        print("The multiplication of two number is\n",n2*n3)
elif n1=="+":
    if n2==56 and n3==9:
        print(77)
    elif n2==9 and n3==56:
        print(77)
    else:
        print("The addition of two number is\n",n2+n3)
elif n1=="/":
    if n2==56 and n3==6:
        print(4)
    elif n2==6 and n3==56:
        print(4)
    else:
        print("The division of two number is\n",n2/n3)
else:
    print("Invalid Input")