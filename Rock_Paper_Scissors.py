import random

game_choices = {'r': '🪨', 'p': '📃', 's': '✂'}

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper or Scissors?(r/p/s): ").lower()
        if user_choice in game_choices.keys():
            return user_choice
        else:
            print('Invalid Choice!')

def display_choices(computer_choice, user_choice):
    print('Computer Chose: ', game_choices[computer_choice])
    print('You Chose: ', game_choices[user_choice])

def determine_winner(computer_choice, user_choice):
    if user_choice==computer_choice:
        print('Its a draw!')
    elif ((user_choice == 'r' and computer_choice == 's') or
         (user_choice == 'p' and computer_choice == 'r') or
         (user_choice == 's' and computer_choice == 'p')):
        print('You Win!')
        should_continue = input('Continue?(y/n): ').lower()
        if should_continue == 'n':
            exit()
    else:
        print('You Lose!')

def play_game():
    while True:
        computer_choice = random.choice(list(game_choices.keys()))
        user_choice = get_user_choice()

        display_choices(computer_choice, user_choice)
        determine_winner(computer_choice, user_choice)

play_game()



