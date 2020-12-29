'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
import random
total_heads = 0
total_tails = 0
for i in range(50):
    num=random.randint(0,1)
    if num==0:
        total_heads += 1
        print("heads")
        print()
    else:
        total_tails += 1
        print("tails")
        print()
print("Number of heads: ",total_heads)
print("Number of tails: ",total_tails)








