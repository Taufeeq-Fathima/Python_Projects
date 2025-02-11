import numpy as np

#initialize variables
pattern = ('-'*3+'+')*3
Players = ['X', 'O']


# Function to take inputs from player
def get_player_input(player, matrix):
    # Exception block to handle type conversion errors
    try:
        row = int(input('Enter row (0-2): '))
        column = int(input('Enter column (0-2): '))

        # Row and column values should be between 0, 2
        if row not in range(3) or column not in range(3):
            print('Invalid range! Please enter a number between (0,2)')
            get_player_input(player, matrix)

        elif matrix[row][column] == ' ':
            matrix[row][column] = player

        else:
            print('Invalid row/column! User input already present')
            get_player_input(player, matrix)

    except ValueError:
        print('Please enter numbers between (0,2)')
        get_player_input(player, matrix)



# Function to display the game with inputs entered by player
def display_players_input(player, matrix):
    print(f"Player {player}'s turn")
    get_player_input(player, matrix)
    for i in range(3):
        print(pattern[:-1])
        print(' ' + ' | '.join(matrix[i]))
    print(pattern[:-1])


# This function will be called only if at least one player has given their inputs for 3 times
# This function will determine if the winner is 'X' or 'O' and call display_winner function
def determine_winner(inp,matrix):
    # Initializing variables
    concat_list = []
    a, b, c, d = '', '', '', ''

    # Creating a list by concatenating the row values and column values
    for i in range(3):
        a = ''.join(matrix[i])      # Row concatenation
        b = ''.join(matrix[:,i])    # Column concatenation
        concat_list.extend([a,b])

    # concatenating the values in diagonals
    c = ''.join(matrix.diagonal())
    d = ''.join(np.fliplr(matrix).diagonal())

    # Appending diagonal values to the list
    concat_list.extend([c,d])

    # Checking the winner

    # if both win then it is a draw so call display_winner without a player
    if 'XXX' in concat_list and 'OOO' in concat_list:
        if inp==4: display_winner(None)

    # When 'O' is the winner
    elif 'OOO' in concat_list:
        display_winner(Players[1])
        continue_game()

    # When 'X' is the winner
    elif 'XXX' in concat_list:
        display_winner(Players[0])
        continue_game()

    # if there is no winner
    else:
        if inp==4: display_winner(None)


# Function to display if it is a win or a draw
def display_winner(player):
    if player is None:
        print("It's a Draw")
    else:
        print(f'Player {player} wins!! Congratulations!')


def continue_game():
    con=input('Do you want to continue(y/n)?: ')
    if con=='n':
        exit()
    else:
        play_game()

# Function to start game
def play_game():
    # Creating a 3*3 Matrix
    matrix = np.array([[" ", " ", " "] for i in range(3)])

    # Take user input to fill Matrix
    for i in range(5):
    # Taking input for 'X'
        display_players_input(Players[0], matrix)

        # Keep checking if there is a winner if a user has given input at least 3 times
        if i>1: determine_winner(i,matrix)

    # Taking input for 'O'
        if i<4: # Player 'O' only enters the values 4 times
            display_players_input(Players[1], matrix)
            if i>1: determine_winner(i,matrix)
        else:
            break

# run function to start game
play_game()





