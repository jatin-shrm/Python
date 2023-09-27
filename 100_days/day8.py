#BlackJack Game
import random
cards=[1,2,3,4,5,6,7,8,9,10,10,10,10,'A']
your_card=[]
# game_play=input("DO you want to play game. Type \'y\' or \'n\': ")
for i in range(2):
    cards_choice=random.choice(cards)
    if cards_choice=='A':
        choice=input("What you wanna choose \'1\' or \'11\': ")
        if choice=='1':
            cards_choice=1
        else:
            cards_choice=11
    
    your_card.append(cards_choice)

print(f"Your crads: {your_card}, current score {sum(your_card)}")