#This file is a Oregan Trail project. Each file will have a text
#document that instructs the user.
#this is the introduction to Oregon Trail
#set all characters in the option menu to Y or N!!!!!

import cmd
import textwrap
import sys
import os
import time

##### Title screen #####
def title_screen_selections():
    option = input(">")
    if option.lower() ==("play"):
        intro()
    elif option.lower() == ("help"):
        instructions()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        title_screen()
        option = input(">")
       
def title_screen():
    #os.system('clear')
    print('##############################')
    print('# Welcome to Oregan Trail #')
    print('##############################')
    print('         -Play-           ')
    print('         -Help-           ')
    print('         -Quit-           ')
    print('  Copyright 2021 CratozStudios   ')
    title_screen_selections()
    
    
def intro():
    name=input("What is your name traveler?: ")
    for characters in name:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.10)
    while name == '':               #stops player from skipping scenes
       print("Please enter a valid name.")
       name=input("What is your name traveler?: ")
       
    age=(input("Enter your age: "))
    for characters in age:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.10)
    while age == '':   #stops player from skipping scenes
        print("Please enter a valid age.")
        age=(input("Enter your age: "))
    print("In this world, you must travel 100 miles in order\nto save the land of Kaiden")
    print("Now inhabited by giant worms, the citizens in the village are terrified\n the town is in complete chaos.")
    print("so",name,"using your instincts and wisdom save this town.")
    intro_file=open("intro.txt", "w")
    intro_file.write(name)
    intro_file.write(age)
    intro_file.close()

#instructions screen!!
def instructions():
    instructions=input("Would you like to read the instructions file?\n y or n ")
    if instructions.lower() == "y":
        instruct=open("instructions.txt", "r")
        print("Read carefully it could save your life.")
        print(instruct.read())
        instruct.close()
    else:
         print("Good Luck on your adventure.")
         title_screen()
         title_screen_selections()
    
def Chapter1():
    print("The land of Kaiden has been under King Techlead for 85 years.")
    print("It is your job to reach the King Techlead and convince\n him to send reinforcements to save the village.")
    print("A old man approaches you with a face filled with dispair..")
    choice=input("Will you talk to him?: Y or N")
    while choice.lower() not in ['Y', 'N', 'y', 'n']:
        print("Please enter a valid command.")
        choice=input("Will you talk to him?: Y or N " )    
    if choice.lower() == "Y" or choice.lower() == "y":
        print("He looks up at you silent before pointing to the village where worms and flames engulf a nearby farm.\n before leaning against your horse from exhaustion.")
        print("The old man introduces himself as Gerim, and hoists himself on your carriage with a map\n with directions to the kingdom before passing out. It seems you have no choice.")
    else:
        print("As you proceed passed the old man, he drops to the ground but from the distant a local villager charges at you pleading for help.")
        print("Sir please!! You look like a strong man go to the king and tell him we can't win against these worms!")
      
def coin_toss():
    import random
    toss= random.randint(1,2)
    print("Now being stuck with Gerim you study the map closely whilist playing\n with a silver coin in your pocket.")
    coin=input("Will you flip the coin? Y or n  ")
    while coin.lower() not in ['y', 'n']:
        print("We don't have all day, can we go now? ")
        coin=input("Will you flip the coin? Yes or no ")
    if coin == "Yes" or coin == "y": 
        if toss == 1:
            print("Heads! \n")
            print("You smile as you continue on your journey.")
            import Travel
            from Travel import road
            road()
            
        else:
            print("Tails!\n")
            print("You start to feel a weird sensation at the bottom of your pit.")
            import Merchant_shop
            Merchant_shop()
        
    if coin == 'n':
        print("you smile while placing the coin back in the pocket.")
        road()


title_screen()
Chapter1()
coin_toss()
