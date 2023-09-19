#Write a program to find how many times substring “Emma” appears in the given string.
str_x = "Emma is good developer. Emma is a writer"
num=str_x.split()
size=len(num)
count=0
for i in range(size):
    word=num[i]
    if word=="Emma":
        count+=1
print(f"Emma appears {count} times")

#or 
print(str_x.count("Emma"))