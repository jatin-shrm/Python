from functools import reduce
list1=[1,2,3,4,5]
#Reduce function used to apply a particular function passed in
# its argument to all of the list elements mentioned in the sequence passed along.
num=reduce(lambda x,y:x+y,list1)
print(num)