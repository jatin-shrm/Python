#hangman game
import random
word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure' 
]

#computer choice
computers_letter=random.choice(word_list)


#Creating blanks
ans=[]
for i in range(len(computers_letter)):
    ans.append("_")

hangman=False

#len of compyer choice
word_length=len(computers_letter)
lives=word_length+3



while not hangman:
    guess=input("Guess the letter: ").lower()

    #if guess is already guessed
    if guess in ans:
        print(f"You have already guessed {guess} letter")



    #if guess is correct
    for position in range(word_length):
        letter=computers_letter[position]
        if letter==guess:
            ans[position]=letter

    #if guess is incorrect
    if guess not in computers_letter:
        
        lives-=1
        if lives==0:
            hangman=True
            print(f"You loose")   
        print(f"You guessed {guess}, that's not in the word. You have only {lives} life.")
    print(f"{' '.join(ans)}")

if "_" not in ans:
    hangman=True
    print("You win")