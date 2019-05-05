import random
import sys
import math

board = ['-','-','-','-','-','-','-','-','-']
available_space = {0,1,2,3,4,5,6,7,8}


def show_board():
    print board[0],',',board[1],',',board[2]
    print board[3],',',board[4],',',board[5]
    print board[6],',',board[7],',',board[8],'\n\n'


def check_end(char):
    if any(board[i] == board[i+3] == board[i+6] == char for i in range(3)):
        return  True
    if board[0] == board[1] == board[2] == char:
        return True
    if board[3] == board[4] == board[5] == char:
        return True
    if board[6] == board[7] == board[8] == char:
        return True
    if board[0] == board[4] == board[8] == char:
        return True
    if board[2] == board[4] == board[6] == char:
        return True

def minimax(position, available_space, maxplayer, board):
    available_space = available_space - {position}
    if check_end('x'):
        return 1
    elif check_end('o'):
        return -1
    elif not available_space:
        return 0
    if maxplayer:
        bestValue = -10
        for i in available_space:
            # board[i] = 'o'
            # if check_end('o'):
            #     return -1
            v = minimax(i, available_space, False, board)
            bestValue = max(v, bestValue)
            # board[i] = '-'
        return bestValue

    if not maxplayer:
        bestValue = 10
        for i in available_space:
            # board[i] = 'x'
            # if check_end('x'):
            #     return 1
            v = minimax(i, available_space, True, board)
            bestValue = min(v, bestValue)
            # board[i] = '-'
        return bestValue


while (available_space):
    finding = True
    while(finding):
        finding = True
        s = int(sys.argv[1])
        random.seed(s)
        while True:
            check = False
            random_position = []
            for i in range(5):
                random_position.append(math.floor(9 * random.random()))
            for length in range(5):
                m = int(random_position[length])
                if m not in available_space:
                    continue
                else:
                    check = True
                    break
            if check == True:
                break
        player_x = m
        if player_x in range(0,9) and board[player_x] == '-':
            board[player_x] = 'x'
            show_board()
            if check_end('x'):
                break
            available_space = available_space - {player_x}
            finding = False
    if check_end('x'):
        break
    min_heur_value = [10] * 9
    for ind in available_space:
        board_copy = board[:]
        board_copy[ind] = 'o'
        min_heur_value[ind] = minimax(ind, available_space, False, board_copy)
    player_o = min_heur_value.index(min(min_heur_value))
    board[player_o] = 'o'
    show_board()
    if check_end('o'):
        break
    available_space = available_space - {player_o}





