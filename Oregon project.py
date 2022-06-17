#this is a template on creating an oregon trail project.
#I will use this to learn and understand the fundamentals of programming.
##this file represents the mechanics of the game.
import random

#constants list
MONTHS_WITH_31_DAYS = [1,3,5,7,8,10,12]
MONTHS_WITH_30_DAYS = [4,6,9,11]
MONTHS_WITH_28_DAYS = [2]
MIN_MILES_PER_TRAVEL = 30
MAX_MILES_PER_TRAVEL = 60
MIN_DAYS_PER_TRAVEL = 3
MAX_DAYS_PER_TRAVEL = 7
TOTAL_MILES = 2000
MAX_HEALTH_LEVEL = 5
MIN_DAYS_PER_REST = 2
MAX_DAYS_PER_REST = 5
MAX_DAYS_PER_HUNT = 5
MIN_DAYS_PER_HUNT = 2

#model variables - game status variables #setting up the initial loop
TotalMilesTraveled = 0
food = 500
health = 5
day = 1
month = 3
year = 0
gameStatus = ''
userCommand = ''


def print_no_valid_command():

    print('The command you have entered is not recognized, please enter a new command.')
    print('what would you like to do? (travel / rest / hunt / status / help / quit)')


def add_day():

    #create degenerative effects
    global food
    food -= 5

    global health

    
    global day
    global month
    global year

    if day == 14 or day == 18:
        health -= 1

    day += 1

    if day >= 28 and MONTHS_WITH_28_DAYS:
        day = 1
        month += 1

    elif day >= 30 and MONTHS_WITH_30_DAYS:
        day = 1
        month += 1

    elif day >= 31 and MONTHS_WITH_31_DAYS:
        day = 1
        month += 1

    if month > 12:
        month = 1
        day = 1
        year = 1


def handle_travel():
    global TotalMilesTraveled

    randomMilesTraveled= random.randint(MIN_MILES_PER_TRAVEL, MAX_MILES_PER_TRAVEL)

    TotalMilesTraveled += randomMilesTraveled
    milesremaining = TOTAL_MILES - TotalMilesTraveled

    print()
    print("You traveled " + str(randomMilesTraveled) + " for a total of " + str(TotalMilesTraveled) + "total miles traveled!")
    print("You have " + str(milesremaining) + " miles left to go until Oregon. ")
    print()

    randomDaysTraveled = random.randint(MIN_DAYS_PER_TRAVEL, MAX_DAYS_PER_TRAVEL)

    for day in range(randomDaysTraveled):
        add_day()


def handle_rest():
    global health

    if health < MAX_HEALTH_LEVEL:
        
        health += 1
        randomDaysResting = random.randint(MIN_DAYS_PER_REST, MAX_DAYS_PER_REST)

        for day in range(randomDaysResting):
            add_day()

        print("You have rested for " + str(randomDaysResting) + " and your health is " + str(health))
    
    else:
        print("You are fully healed you do not need to rest")

def handle_hunt():
    global food
    food += 100

    randomDaysHunting = random.randint(MIN_DAYS_PER_HUNT, MAX_DAYS_PER_HUNT)

    for day in range(randomDaysHunting):
        add_day()

    print("You take " + str(randomDaysHunting) + " days to collect 100 pounds of food. ")


def handle_help():
    print("Pay more attention next time.")
def handle_status():
    
    global month
    global day
    global TotalMilesTraveled
    global health
    global food

    print("and your health is " + str(health))
    print("You have " + str(food) + " total pounds of food. ")

    milesremaining = TOTAL_MILES - TotalMilesTraveled

    print()
    print("You traveled a total of" + str(TotalMilesTraveled) + " total miles traveled! ")
    print("You have " + str(milesremaining) + " miles left to go until Oregon.")
    print()

    print("It is day " + str(day) +" of month " + str(month))

    pass

def check_status():

    global year
    global food
    global health

    if year >= 1:
        handle_loss()
    
    elif health < 1:

        handle_loss()

    elif food < 1:

        handle_loss()

def handle_loss():

    check_status()
    handle_quit()

def handle_quit():

    global gameStatus
    gameStatus = "game over"

print(welcome_text)
print()


while gameStatus != "game over" and userCommand != 'quit':

    #check to see if the user has won or loss
    check_status()

    userCommand = input('what would you like to do? (travel / rest / hunt / status / help / quit) ')
#if commands following the players actions with handled functions
    if userCommand == 'travel':
        handle_travel()

    elif userCommand == 'rest':
        handle_rest()

    elif userCommand == 'hunt':
        handle_hunt()

    elif userCommand == 'status':
        handle_status()

    elif userCommand == 'help':
        handle_help()

    elif userCommand == 'quit':
        handle_quit()

    else:
        print_no_valid_command()
