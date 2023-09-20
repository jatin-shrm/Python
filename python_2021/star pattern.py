# No of rows that you want to print in your pattern
n = int(input("Enter the number of rows\n"))
# patter deciding factor, if the output is True then pattern will be, for example for
# three rows
#        *
#        **
#        ***
# and if the ouput is false the pattern will be
#        ***
#        **
#        *
n1 = int(input("Enter 0 or 1\n"))
if n1 == True:
    for i in range(0, n + 1):
        print("* "*i)
elif n1 == False:
    for i in range(n, 0, -1):
        print("* " * i)
else:
    print("Invalid Input\nTry again")
