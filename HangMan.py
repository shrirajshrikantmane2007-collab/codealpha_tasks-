# Importing libraries 
import random
import pyfiglet
import time
import colorama

# Giving tilte 
title=pyfiglet.figlet_format("WELCOME HANGMAN !!")
print(title)

# Checking whether user is ready for game or not 
choice=input("⚪ \033[94m Shall we start game ? [Y/N] :: \033[0m")

# Health points 
Health=["🚨","🚨","🚨","🚨","🚨","🚨"]


# Declaring a list of words 
words=["hello","best","codealpha","guess","birthday"]

if(choice=='Y' or choice =='y' ):
    # Choosing word randomly 
    a=random.choice(words)

    # Pre-warning 
    print("Ready ? Game will start in 2 seconds ")
    for i in range(4):
        print(".",end="")
        time.sleep(0.5)
    print("\n")


    # Creating another string (guessed one )
    guess=set()

    # Running the loop to get input until user win or loose 
    while True:


        # printing the health points remaining 
        print(f"\nHealth: {len(Health)} ", end="")
        for i in Health :
            print(i,end='')


        # Taking input from user 
        b=input("\033[93m\nGuess letter :: \033[0m")

        # Adding the letter to guessed word if present in real word
        if b in a :
            guess.add(b)

        # Checking guessed word is correct or not 
        if all(letter in guess for letter in a ):
            # If word is correct then announce user as Winner 
            if len(guess)>=len(a):
                print("Congratulations  !! You win the game .")
                print("The word is ::",a)
                break

        # Giving responce if entered letter is present in word or not 
        if b in a:
            print("\033[92mGreat !! You entered correct letter . ")


        #If entere letter is wrong then reducing health points and messaging that letter is wrong 
        else:
            print("\033[91mWrong Attempt .\033[0m")
            if len(Health)>1:
                Health.pop()
            else:
                print("You lost the game .. Try again .")
                break


else:
    print("Ok prepare for game .")
