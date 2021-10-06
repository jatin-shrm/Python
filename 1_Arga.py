def args(another,*args):
    print(another)
    for i in args:
        print(i)
list1=["Jatin","Parth","Anirudh","Aditya","Soheb"]
another="Here another is a normal argument"
args(another,*list1)