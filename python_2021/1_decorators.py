def dec1(func1):
    def nowjatin():
        print("Executing now")
        func1()
        print("Executed")
    return nowjatin
@dec1()
def I_am_Jatin():
    print("I am Jatin")
I_am_Jatin()