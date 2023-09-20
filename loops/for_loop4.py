#Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
num=int(input("Enter the number: "))
sum=0
temp=0
for i in range(num):
    temp=(temp*10)+2
    sum+=temp
    print(temp)
print(sum)