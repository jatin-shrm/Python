number_of_guesses=1
while(number_of_guesses<=9):    
     n=int(input("Enter the number\n"))    
     if n>18:
        print("You have entered the greater number\nTry Again")  
     elif n<18:
        print("You have enterd the smaller number\nTry Again")  
     else:
        print("You Win\nNumber of guesses you took to win is equal to ",number_of_guesses)
        break        
     print(9-number_of_guesses,"no of guesses left")
     number_of_guesses=number_of_guesses+1
if number_of_guesses>9:
    print("Game Over")