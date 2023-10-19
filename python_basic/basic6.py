#match case
x=int(input("Enter the value of x: "))
match x:
    case 0:
        print("This is 0")
    case 1:
        print("This is 1")
    case 2:
        print("This is 2")
    case 3:
        print("This is 3")
    case _:
        print("This is default")