from google.colab import output

MARK1 = 'O'
MARK2 = 'X'


def print_ui(table, player1, player2, score1, score2):

    print('-----------------------Score Board-----------------------')
    print(f"{player1}: {score1}")
    print(f"{player2}: {score2}")
    print('---------------------------------------------------------')   

    print()

    print('------------------Your Tic Tac Toe Table------------------')
    for i in range(len(table)):
        for j in range(len(table[0])):
            print(table[i][j], end=" ")
        print()
    print()
    print('----------------------------------------------------------')
    
    print()


def check_win(table, player1, player2):

    winning_player = 0

    # check for rows
    row_count_for_o = 0
    row_count_for_x = 0
    for r in table:
        for item in r:
            if item == "O":
                row_count_for_o += 1

            elif item == "X":
                row_count_for_x += 1

        if row_count_for_o == 3:
            winning_player = 1
            return winning_player

        elif row_count_for_x == 3:
            winning_player = 2
            return winning_player

        row_count_for_o = 0
        row_count_for_x = 0

    # check for each column
    col_count_for_x = 0
    col_count_for_o = 0
    for r in range(len(table)):
        for item in range(len(table[0])):
            if table[item][r] == 'O':
                col_count_for_o += 1
            elif table[item][r] == 'X':
                col_count_for_x += 1

        if col_count_for_o == 3:
            winning_player = 1
            return winning_player
        elif col_count_for_x == 3:
            winning_player = 2
            return winning_player

        col_count_for_x = 0
        col_count_for_o = 0

    # check for diagnol win

    # # left to right diagnol
    left_diagnol_count_for_o = 0
    left_diagnol_count_for_x = 0
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][i] == 'O':
                left_diagnol_count_for_o += 1
                break
            elif table[i][i] == 'X':
                left_diagnol_count_for_x += 1
                break
                
        if left_diagnol_count_for_o == 3:
            winning_player = 1
            return winning_player
        elif left_diagnol_count_for_x == 3:
            winning_player = 2
            return winning_player

    # right diagnol
    right_diagnol_count_for_o = 0
    right_diagnol_count_for_x = 0
    for i in range(len(table)):
        if table[i][len(table)-i-1] == "O":
            right_diagnol_count_for_o += 1
            
        elif table[i][len(table)-i-1] == "X":
            right_diagnol_count_for_x += 1

        if right_diagnol_count_for_o == 3:
            winning_player = 1
            return winning_player
        elif right_diagnol_count_for_x == 3:
            winning_player = 2
            return winning_player

def tic_tac_toe():

    MARK1 = 'O'
    MARK2 = 'X'

    player1_score = 0
    player2_score = 0

    ask_players = True

    eol = True
    while eol:
        if ask_players == True:
            player1 = input(f"Player 1, enter you name(your mark: {MARK1}): ")
            player2 = input(f'Player 2, enter your name(your mark: {MARK2}): ')
            player1_score = 0
            player2_score = 0

        current_player = ""
        current_player_mark = ""
        current_player_identifier = 0
        the_winner_of_game = ""

        winner = -1

        table = [['_', '_', '_'],
                ['_', '_', '_'],
                ['_', '_', '_']]

        check_table = [[False, False, False],
                        [False, False, False],
                        [False, False, False]]

        playing_game = True
        while playing_game:

            output.clear()
            print_ui(table, player1, player2, player1_score, player2_score)

            if current_player_identifier % 2 == 0:
                current_player = player1
                current_player_mark = MARK1
            else:
                current_player = player2
                current_player_mark = MARK2

            current_player_identifier += 1

            print(f"---------{current_player}'s Turn---------")
            print('Where do you want to place your mark?')
            print("Enter 'Exit' to quit")

            place = input('(e.g., 2 1)(2 is row and 1 is column): ')

            if place == "Exit" or place == 'exit':
                playing_game = False
                break
            arr = place.split()
            row = int(arr[0]) - 1
            column = int(arr[1]) - 1

            if check_table[row][column] == True:
                print('Place Already Occupied.')
                current_player_identifier += 1
                continue
            else:
                table[row][column] = current_player_mark
                check_table[row][column] = True

            winner = check_win(table, player1, player2)
            if winner == 1:
                player1_score += 1
                the_winner_of_game = player1
                playing_game = False
                break
                
            elif winner == 2:
                player2_score += 1
                the_winner_of_game = player2
                playing_game = False
                break

            if False not in check_table[0] and False not in check_table[1] and False not in check_table[2]:
                winner = 0
                break


        output.clear()
        print_ui(table, player1, player2, player1_score, player2_score)


        if winner == 1 or winner == 2:
            print(f"{the_winner_of_game} wins")
        elif winner == 0:
            print('Draw')
        else:
            print('Game was left before winner could be decided.')

        play_again = input('Want to play again?(y/n): ').lower()
        if play_again == 'y':
            same_players = input('Continue with same players?(y/n): ').lower()
            if same_players == 'y' or same_players == 'yes':
                ask_players = False
            else:
                ask_players = True
            output.clear()
            continue
        else:
            print('Game quit successfully')
            eol = False


ask = input('Do you want to play tic tac to?(y/n): ').lower()
if ask == 'y':
    output.clear()
    tic_tac_toe()
else:
    print('Program exit successfully.')
