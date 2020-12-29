'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
done = False
miles_traveled=0
thirst=0
camel_tiredness=0
natives=60
drinks_in_canteen=6
oasis= random.randint(1,20)
while not done:

    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit")
    user_input=input("What is your choice?: ")
    
    if user_input.upper() == "Q": #quit
        print("Thanks for playing!")
        done = True
    elif user_input.upper() == "E":  #status check
        print("You have traveled:",miles_traveled,"miles.")
        print("You have",drinks_in_canteen,"drinks left")
        print("The natives are",natives,"miles behind you")

    elif user_input.upper() == "D": #stop for night
        camel_tiredness = 0
        natives -= random.randint(7,14)
        print("Your camel's tiredness is:", camel_tiredness)
        print("Camel is happy!")
        print("The natives are",natives,"miles behind you.")

    elif user_input.upper() == "C": #full speed
        miles_traveled += random.randint(15,30)
        thirst += 1
        camel_tiredness += random.randint(1,3)
        natives -= random.randint(7, 14)
        print("You have traveled:",miles_traveled,"miles")
        print("Your thirst is",thirst)
        print("Your camel's tiredness is:",camel_tiredness)
        print("The natives are:",natives,"miles behind you")

    elif user_input.upper() == "B": #moderate speed
        miles_traveled += random.randint(10,15)
        natives -= random.randint(7, 14)
        thirst += 1
        camel_tiredness += 1
        print("You have traveled:", miles_traveled, "miles")
        print("Your thirst is", thirst)
        print("Your camel's tiredness is:", camel_tiredness)
        print("The natives are:", natives, "miles behind you")

    elif user_input.upper() == "A": #drink from canteen
        if drinks_in_canteen > 0:
            drinks_in_canteen -= 1
            thirst=0
            print("You have:",drinks_in_canteen,"drinks left")
        else:
            print("Your canteen is empty")

    oasis: int = random.randint(1, 5)

    if oasis == 1:
        drinks_in_canteen = 6
        thirst = 0
        camel_tiredness = 0
        print("You found an oasis!!")
        print("You've refilled your canteen")

#thirst warnings
    if not done and thirst > 6:
        print("You died of thirst!")
        print("Thank you for playing!")
        done = True
    elif not done and thirst > 4:
        print("You are thirsty")

#camel tiredness warning
    if not done and camel_tiredness > 8:
        print("Your camel died!")
        print("Thank you for playing!")
        done =True
    elif not done and camel_tiredness > 5:
        print("Your camel is dead!")

#natives distance
    if not done and natives <= 0:
        print("The natives have caught up!")
        print("Thank you for playing!")
        done = True
    elif not done and natives < 15:
        print("The natives are close")

#if crossed desert
    if not done and miles_traveled == 200:
        print("You won!!!")
        print("Thank you for playing!")
        done = True


















