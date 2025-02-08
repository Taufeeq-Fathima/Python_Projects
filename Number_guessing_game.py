import random

i=1
random_number = random.randint(1, 100)
while i!=0:
    inp = int(input('Guess the number between 1 to 100: '))
    if inp not in range(1,101):
        print('Please enter a valid number')
    elif inp>random_number:
        print('Too High')
    elif inp<random_number:
        print('Too Low')
    elif inp==random_number:
        print('Congratulations! You guessed the number.')
        i=0
        break

