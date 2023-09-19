#Print characters from a string that are present at an even index number
string=input("Enter your string: ").lower()
size=len(string)
for i in range(size):
    if(i%2)==0:
        print(string[i])