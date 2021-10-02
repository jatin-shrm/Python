def fibonacci(n):
    if n==1:
        return 1
    else:
        return n + fibonacci(n-1)
num=int(input("Enter the number\n"))
print(fibonacci(num))