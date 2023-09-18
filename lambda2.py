def fibonacci(n):
    if n==1:
        return 1
    else:
        return fibonacci(n-2)+ fibonacci(n-1)
num=int(input("Enter the number\n"))
print(fibonacci(num))