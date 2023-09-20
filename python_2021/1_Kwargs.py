def kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"Role of {key} is to handle {value}")
list1={"Jatin":"Monitor","Parth":"Council Members","Anirudh":"Sports commeties","Aditya":"Cultural events"}
kwargs(**list1)