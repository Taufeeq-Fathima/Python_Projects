import numpy as np

#initialize variables
pattern = ('-'*3+'+')
Players = ['X', 'O']


# Function to take inputs from player
def get_player_input(player):
    # Exception block to handle type conversion errors
    while True:
        try:
            row = int(input(f'Enter row (1-{board_size}): ')) - 1
            column = int(input(f'Enter column (1-{board_size}): ')) - 1

            # Row and column values should be between 0, 2
            if row not in range(board_size) or column not in range(board_size):
                print(f'Invalid range! Please enter a number between (1,{board_size})')
                continue

            elif matrix[row][column] == ' ':
                matrix[row][column] = player
                break

            else:
                print('Invalid row/column! User input already present')
                continue

        except ValueError:
            print(f'Please enter numbers between (1,{board_size})')
            continue


# Function to display the game with inputs entered by player
def display_players_input(player):
    print(f"Player {player}'s turn")
    get_player_input(player)
    for i in range(board_size):
        print((pattern * board_size)[:-1])
        print(' ' + ' | '.join(matrix[i]))
    print((pattern * board_size)[:-1])


# This function will be called only if at least one player has given their inputs for 3 times
# This function will determine if the winner is 'X' or 'O' and call display_winner function
def determine_winner():
    # Initializing variables
    concat_list = []
    a, b, c, d = '', '', '', ''

    # Creating a list by concatenating the row values and column values
    for i in range(board_size):
        a = ''.join(matrix[i])      # Row concatenation
        b = ''.join(matrix[:,i])    # Column concatenation
        concat_list.extend([a,b])

    # concatenating the values in diagonals
    c = ''.join(matrix.diagonal())
    d = ''.join(np.fliplr(matrix).diagonal())

    # Appending diagonal values to the list
    concat_list.extend([c,d])

    # Check for a winner
    if Players[0] * board_size in concat_list:  # Player 'X' wins
        display_winner(Players[0])
    elif Players[1] * board_size in concat_list:  # Player 'O' wins
        display_winner(Players[1])
    elif not np.any(matrix == ' '):  # No more empty spaces, it's a draw
        display_winner(None)


# Function to display if it is a win or a draw
def display_winner(player):
    if player is None:
        print("It's a Draw")
    else:
        print(f'Player {player} wins!! Congratulations!')
    continue_game()


def continue_game():
    while True:
        con = input('Do you want to continue(y/n)?: ').lower()
        if con == 'n':
            exit()
        elif con == 'y':
            play_game()
            break
        else:
            print("Invalid input! Please enter 'y' or 'n'.")


# Function to start game
def play_game():
    # Creating a 3*3 Matrix

    global matrix, board_size, user_input_count
    while True:
        try:
            board_size = int(input('What board size do you want to play?(3/4/5): '))
            if board_size not in (3,4,5):
                print('Error! Please enter a board size between (3/4/5)')
                continue
            break
        except ValueError:
            print('Error! Please enter a board size between (3/4/5)')
            continue

    matrix = np.full((board_size, board_size), " ")

    # Start the game loop, alternating between players
    current_player_index = 0
    while True:
        current_player = Players[current_player_index % 2]  # Alternate players 'X' and 'O'
        display_players_input(current_player)

        # Check for a winner after each move
        if determine_winner():
            break

        current_player_index += 1  # Move to the next player

# run function to start game
play_game()