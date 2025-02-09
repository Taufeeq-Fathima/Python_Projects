## case 1:
## case 2:
## case 3:
## case 4:
import random

i = 1
d = { 'r':'🪨','p':'📃','s':'✂'}

def print_details():
    print('Computer Chose: ', d[k])
    print('You Chose: ', d[inp])

while i != 0:
    inp = input("Rock, Paper or Scissors?(r/p/s): ")
    k = random.choice(list(d.keys()))
    if inp not in d.keys():
        print('Invalid Choice!')
        continue
    elif inp == 'r' and k == 'p':
        print_details()
        print('You Lose!')
        continue
    elif inp == 'r' and k == 's':
        print_details()
        print('You Win!')
    elif inp == 'p' and k == 'r':
        print_details()
        print('You Win!')
    elif inp == 'p' and k == 's':
        print_details()
        print('You Lose!')
        continue
    elif inp == 's' and k == 'r':
        print_details()
        print('You Lose!')
        continue
    elif inp == 's' and k == 'p':
        print_details()
        print('You Win!')
    else:
        print_details()
        print('Its a draw!')
        continue
    con = input('Continue?(y/n): ')
    if con == 'y':
        i = 1
    elif con == 'n':
        i = 0
    else:
        print('Invalid Choice!')

