def args(another,*args):
    print(another)
    for j in args:
        print(j)
list1=["Jatin","Parth","Anirudh","Aditya","Soheb"]
another="Here another is a normal argument"
args(another,*list1)
