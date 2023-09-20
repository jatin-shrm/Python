#Filter function allows you to process an iterable and extract those items that satisfy a given condition.
list1=[5,8,22,56,33,86,33]
def is_greater_then_17(num):
    return num>17
gr_than_17=list(filter(is_greater_then_17,list1))
print(gr_than_17)