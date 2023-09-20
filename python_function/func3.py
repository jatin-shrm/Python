#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
ans=0
def add(num):
    if num>0:
        return  add(num-1) + num 
    else:
        return 0
number=int(input("Enter the number: "))
print(add(number))