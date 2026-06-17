# importing libraries

import pyfiglet
import time
import colorama

a=pyfiglet.figlet_format("PYTHOBOT")
print("\033[91m"+a)

print("\033[92mWelcome !! Hi ..\033[0m")
 

dict={
    "Hello":"How are you !",
    "I am fine .":"Oh ok .",
    "How are you ?":"I am fine .",
    "What about you ?":"I am also fine .",
    "I am sad .":"Be optimistic all will well !"
}

while True:
    user=input("You : ").capitalize()
    if user in dict:
        print("Bot :",dict[user])
    elif user=="Bye":
        print("Ok bye .")
        break
    else:
        print("Please enter valid input !")