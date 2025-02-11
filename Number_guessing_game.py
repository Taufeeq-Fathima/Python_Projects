import random
from sys import excepthook

random_number = random.randint(1, 100)

while True:
    try:
        input_number = int(input('Guess the number between 1 to 100: '))
        if input_number not in range(1, 101):
            print('Please enter a number between (1,100)')
        elif input_number > random_number:
            print('Too High')
        elif input_number < random_number:
            print('Too Low')
        else:
            print('Congratulations! You guessed the number.')
            break
    except ValueError:
        print('Please enter a valid number')


