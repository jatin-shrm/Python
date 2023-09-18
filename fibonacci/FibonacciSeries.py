def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci_recursive(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq
num=int(input("Enter the number\n"))
print(fibonacci_recursive(num))