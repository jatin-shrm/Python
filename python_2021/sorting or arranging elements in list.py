list1=[[6,4,5],[4,6,3],[5,3,4],[1,5,9]]
#creating an user defined function for arranging particular element in the lsit
def SortByPlace(element):
#here 2 define the place of elemnts in the list for sorting
    return element[2]
n=list1.sort(key=SortByPlace)
print(list1)