#Turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]
res=[x*x for x in numbers]
# for item in range(len(numbers)):
#     numbers[item]=pow(numbers[item],2)
print(res)