nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num=list(filter(lambda x:x%2==0,nums))
odd_num=list(filter(lambda x:x%2!=0,nums))
print(f"The list containing even number is {even_num}")
print(f"The list containing even number is {odd_num}")