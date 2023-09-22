print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")
side=input("You'r at cross road. Where do you wanna go? Type \"left\" or \"right\"\n").lower()
if (side=="left"):
    lake=input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for the boat. Type \"swim\" to swim across\n").lower()
    if(lake=="wait"):
        color=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if(color=="red"):
            print("It's a room full of fire. Game Over.")
        elif( color=="yellow"):
            print("You found the treasure! You Win!")
        elif(color=="blue"):
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")