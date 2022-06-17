# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 13:57:14 2021

@author: Merida
"""
#this here is the shop modukle
#where the player finds a nearby merchant and buys selected items from him or her.
#This module will later be imported whenever the player is in need of items.

def shop():
    print("While traveling you glimpse of what appears to be a merchant on the side of the road.")
    print("Gerim notices you observing, and tells you this 'You never know when you need supplies..'")
    
    choice=input("Talk to the shady merchant? Y or N ")
    import random
    Gender=random.randint(1,2)
    if choice.lower() == 'Y' or choice.lower() == 'y':
        if Gender == 1: #I am not sure how to make this trading more efficient  #if possible create the shopping to have a number formation.
            print("Instead of you walking towards the merchant, the man quickly marches towards you\n")
            print("With eyes of desperation as if he had stolen all of his goods opens his bag filled\n with various items")
            print("without you saying a word, he whispers in a hoarse voice.'Whaddya buying??..'")
            item_in_stock={'meat':2,'Hide':1,'Wine':1}
            print(item_in_stock)
            buy=input('What item will you buy?' )
            if buy.lower() == 'meat':
                item_in_stock['meat'] - 1
                bag=open('Inventory.txt', 'a')
                bag.write('meat')
                print("Smart move pal!")
                bag.close()
            if buy.lower() == 'Hide':
                item_in_stock['Hide'] - 1
                bag=open('Inventory.txt', 'a')
                bag.write('Hide')
                print("Now that will keep ya warm!")
                bag.close()
            if buy.lower() == 'wine':   #does not work
                item_in_stock['wine'] - 1
                bag=open('Inventory.txt', 'a')
                bag.write('wine')
                print("Live a little have a drink..!")
                bag.close()    
            if item_in_stock == 0:
                print("Sorry I ran out..")
                print("Come back next time.") 
                        
            
        else:
            print("You walk up to the merchant only to find a woman carrying fruit and veggies.")
            print("She looks at you and frown, before you realize that her items are not for sale.")
            print("laughs hysterically from your expression as you embarissingly continue on")
            
            
    else:
        print("You shake your head refusing to stop and decide to carry on with your journey.")
        import Travel
        from Travel import road
        
        
        
#This is the inventory system
#for now it is only accessible when the player has finished shopping with a merchant
#later it will be accessible during conversations with Gerim
        
def inventory():
    pouch=input("Would you like to view your inventory?  Y or  N:   ")
    if pouch == "Y" or pouch == 'y':
        bag=open("Inventory.txt", 'r')
        print(bag.read())
        select_items=input('Use an item?: Y or N  ')
        if select_items == "Y":
            specific_items=input("Which item?  ")
            if specific_items.lower() == "meat":
                print("You have eaten a piece of jerky.")
                bag=open('Inventory.tx', 'a')
                bag.pop('meat')
                bag.close()
            elif specific_items.lower() == "hide":
                print("You now wrapped fox hide over your shoulders for\n additional warmth.")
                bag=open('Inventory.tx', 'a')
                bag.pop('hide')
                bag.close()
            elif specific_items.lower() == "Wine":
                print("You have quenched your thirst.")
                bag=open('Inventory.tx', 'a')
                bag.pop('wine')
                bag.close()
        else:
            print("You've decided to put your pouch away and carried on with your journey.")
            bag.close()       
shop()
inventory()       