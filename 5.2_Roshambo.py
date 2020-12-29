'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random
done = False
win = 0
loss = 0
ties = 0
while not done:

    #user play
    print()
    choice=int(input("Enter the number for what you want: 1: rock, 2: paper, or 3: scissors or 4: Quit: "))
    if choice == 1:
        print("you chose: rock")
    elif choice == 2:
        print("you chose: paper")
    elif choice == 3:
        print("you chose: scissors")
    elif choice == 4:
        done= True
    else:
        print("Incorrect Entry")

    #computer play
    bot= random.randint(1,3)
    if bot == 1:
        print("bot chose: rock")
    elif bot == 2:
        print("bot chose: paper")
    else:
        print("bot chose: scissors")

    #check for tie
    if choice == bot:
        print("tie")
        ties += 1
        
    #if chose rock
    elif choice == 1 and bot == 2:
        print("you lose")
        loss += 1
    elif choice == 1 and bot == 3:
        print("you win")
        win += 1
        
    # if chose paper
    elif choice == 2 and bot == 3:
        print("you lose")
        loss += 1
    elif choice == 2 and bot == 1:
        print("you win")
        win += 1

    # if chose scissors
    elif choice == 3 and bot == 1:
        print("you lose")
        loss += 1
    elif choice == 3 and bot == 2:
        print("you win")
        win += 1

print("Thanks for playing!")
print("Your Win/Loss/Tie Record:",win,"/",loss,"/",ties)









