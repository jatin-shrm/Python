#Calculate the sum of all numbers from 1 to a given number
num=int(input("Enter the number: "))
total=0
for _ in range(num+1):
    total+=_
print(f"Total sum is {total}")