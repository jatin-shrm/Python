#try, exception and finally
# try:
#     x=int(input("Enter any number: "))
# except:
#     print(f"Number is not integer")
# finally:
#     print("Thank you")

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise