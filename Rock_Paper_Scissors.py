import random

choices_dict = {'r': '🪨', 'p': '📃', 's': '✂'}

while True:
    user_choice = input("Rock, Paper or Scissors?(r/p/s): ").lower()
    if user_choice not in choices_dict.keys():
        print('Invalid Choice!')
        continue

    computer_choice = random.choice(list(choices_dict.keys()))

    print('Computer Chose: ', choices_dict[computer_choice])
    print('You Chose: ', choices_dict[user_choice])

    if user_choice==computer_choice:
        print('Its a draw!')
        continue
    elif ((user_choice == 'r' and computer_choice == 's') or
         (user_choice == 'p' and computer_choice == 'r') or
         (user_choice == 's' and computer_choice == 'p')):
        print('You Win!')
        should_continue = input('Continue?(y/n): ').lower()
        if should_continue == 'n':
            exit()
    else:
        print('You Lose!')
        continue




