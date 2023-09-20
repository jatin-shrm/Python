#printing fibonacci series iterative approach
a=-1
b=1
num=int(input("Enter the number: "))
for i in range(1,num+1):
    sum=a+b
    a=b
    b=sum
    print(sum)