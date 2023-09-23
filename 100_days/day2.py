##ROck paper scissors
import random
print("Welcome to the Rock Paper Scissors game\n")
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice=random.randint(0,2)
print(computer_choice)
if user_choice==0:
    if computer_choice==0:
        print(f"Your choice is: ROCK\nComputer's choice is: ROCK\nGame Tie")
    elif computer_choice==1:
        print(f"Your choice is: ROCK\nComputer's choice is: PAPER\nYou loose")
    else:
        print(f"Your choice is: ROCK\nComputer's choice is: Scissors\nYou Win")
elif user_choice==1:
    if computer_choice==0:
        print(f"Your choice is: Paper\nComputer's choice is: ROCK\nYou Win")
    elif computer_choice==1:
        print(f"Your choice is: Paper\nComputer's choice is: PAPER\nGame Tie")
    else:
        print(f"Your choice is: Paper\nComputer's choice is: Scissors\nYou loose")
else:
    if computer_choice==0:
        print(f"Your choice is: Scissors\nComputer's choice is: ROCK\nYou loose")
    elif computer_choice==1:
        print(f"Your choice is: Scissors\nComputer's choice is: PAPER\nYou WIn")
    else:
        print(f"Your choice is: Scissors\nComputer's choice is: Scissors\nGame Tie")