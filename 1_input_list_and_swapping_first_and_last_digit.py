lst=input("Enter the  elements you want in list separated by space\n")
Input_list=lst.split()
print("List befor swapping the first and last digits: ",Input_list)
size=len(Input_list)
print(size)
def function1(Input_list):
    temp=Input_list[0]
    Input_list[0]=Input_list[size-1]
    Input_list[size-1]=temp
    return Input_list
print(function1(Input_list))
