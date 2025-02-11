## 1. Ask user to roll the dice
## 2. Take y/n as input
## 3. If it is not y/n then print “Invalid Input!”
## 4. If it is y then print a pair of random numbers. E.g.: (1,5)
## 5. If it is n then print “Thanks for playing!” and exit the game
import random

# Create a loop to keep asking the user to roll the dice
while True:
    inp = input("Roll the dice? (y/n): ")
    if inp=='y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')
    elif inp=='n':
        print('Thanks for Playing!')
        i=0
        break
    else:
        print('invalid Choice')
        continue
