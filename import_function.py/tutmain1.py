def printjeet(string):
    return f"This my string {string}"
def add(num1,num2):
    return num1 + num2 + 6
#This if__name=='__main__' function implies that : if we import this file, then the code in this function have will not affect the new file, only the code exceptthis fuction is executable
if __name__=='__main__':
    print(printjeet("Jatin"))
    o=add(4,6)
    print(o)
