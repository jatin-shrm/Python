#Write a program to remove characters from a string starting from zero up to n and return a new string.
string=input("Enter your string: ").lower()
size=len(string)
num=int(input("Enter the number of char you want to remove: "))
print(string[num:size])