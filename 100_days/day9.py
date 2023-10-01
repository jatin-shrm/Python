#Number guessing game
import random
computer_number=random.randint(1,100)
print("Welcome to the number guessing game")
print("I am thinking of a number betweeen 1 and 30")
difficulty=input("Choose a difficulty. Type 'easy' and 'hard': ")

attempts=5
def compare(number,com_choice):
    global attempts
    if number>com_choice:
        attempts=attempts-1
        print("Too high")
    elif number<com_choice:
        attempts=attempts-1
        print("Too low")
    else:
        attempts=attempts-1
        print("You win")
        global guessing
        guessing=True
guessing=False
while not guessing:
    print(f"You have {attempts} attempts to pass a number ")
    guess=int(input("Make a guess: "))
    compare(guess,computer_number)
