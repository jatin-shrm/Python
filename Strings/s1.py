#Write a program to create a new string made of an input string’s first, middle, and last character.
string=input("Enter your string: ")
middle_element=int(len(string)/2)
print(string[0]+string[middle_element]+string[-1])