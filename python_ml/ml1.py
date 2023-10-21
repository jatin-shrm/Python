#numpy
import numpy as np
my_list1=[1,2,3,4,5]
#print(my_list1)
arr=np.array(my_list1)
arr.reshape(5,1)
#print(arr)
my_list2=[6,7,8,9,10]
my_list3=[11,12,13,14,15]
arr=np.array([my_list1,my_list2,my_list3])
print(arr[:2,:2])
print(np.linspace(1,10,50))