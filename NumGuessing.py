'''
A fun program that makes u guess a number randomly.
It returns in which count you guessed it properly.
'''

import random

print("Guess the number!")
print("\nI'm thinking of a number from 1 to 10")
c='y'
while c.lower()=='y':
    count=1
    r=random.randint(1,10)
    while True:
        g=int(input("Your guess : "))
        if g>r:
            print("Too high")
        elif g<r :
            print("Too low")
        else:
            print("You guessed it in {} times".format(count))
            break
        count+=1

    c=input("\nWould you like to play again(y/n)? ")
print("\nBye!")
