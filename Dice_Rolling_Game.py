## 1.	Ask user to roll the dice
## 2.	Take y/n as input
## 3.	If it is not y/n then print “Invalid Input!”
## 4.	If it is y then print a pair of random numbers. E.g.: (1,5)
## 5.	If it is n then print “Thanks for playing!” and exit the game
import random

i= 1
while i!=0:
    inp = input("Roll the dice? (y/n): ")
    if inp=='y':
        print(random.randint(1,6),random.randint(1,6))
    elif inp=='n':
        print('Thanks for Playing!')
        i=0
        break
    else:
        print('invalid Choice')
        continue
