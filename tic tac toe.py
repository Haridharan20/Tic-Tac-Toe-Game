from IPython.display import clear_output
import random
def display_board(board):
    clear_output()
    print(' | |')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(' | |')
    print('-----')
    print(' | |')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(' | |')
    print('-----')
    print(' | |')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(' | |')


def player_input():
    '''
    output=(player1 marker,player2 marker)
    '''
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()
    if marker == 'X':

        return ('X','O')
    else:

        return ('O','X')

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    return((board[1] == mark and board[2] == mark and board[3] == mark) or
      (board[4] == mark and board[5] == mark and board[6] == mark)or
      (board[7] == mark and board[8] == mark and board[9] == mark)or
      (board[1] == mark and board[4] == mark and board[7] == mark)or
      (board[2] == mark and board[5] == mark and board[8] == mark)or
      (board[3] == mark and board[6] == mark and board[9] == mark)or
      (board[1] == mark and board[5] == mark and board[9] == mark)or
      (board[7] == mark and board[5] == mark and board[3] == mark))


def choose_first():
    flip = random.randint(0, 1)

    if (flip == 0):
        return 'player1'
    else:
        return 'player2'


def space_check(board, position):
    return board[position] == ' '


def full_board(board):
    for i in range(1, 10):
        if space_check(board, i):  # check for free space
            return False

    # board is full return true
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position (1-9)'))
    return position

def replay(who=None):
    input("play again? Enter yes or no")
    return who =='yes'


print('welcome to game')
while True:

    theboard = [' '] * 10
    player1_marker, player2_marker = player_input()
    print(player1_marker,player2_marker)
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input('ready to play y or n ?')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player1':
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player1_marker, position)
            if win_check(theboard, player1_marker):
                display_board(theboard)
                print('player 1 win')
                game_on = False
            else:
                if full_board(theboard):
                    display_board(theboard)
                    print('tie')
                    game_on = False
                else:
                    turn = 'player2'

        else:
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player2_marker, position)
            if win_check(theboard, player2_marker):
                display_board(theboard)
                print('player 2 win')
                game_on = False
            else:
                if full_board(theboard):
                    display_board(theboard)
                    print('tie')
                    game_on = False
                else:
                    turn = 'player1'

    if not replay():
        break
