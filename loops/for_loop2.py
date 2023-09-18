#Print list in reverse order using a loop
elements=int(input("Enter the no element in the list: "))
Old_list=[]
for i in range(elements):
    element=int(input())
    Old_list.append(element)

print(Old_list)
size=elements-1
new_list=[]

for i in range(size,-1,-1):
    element=Old_list[i]
    new_list.append(element)
print(new_list)