board = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
         'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
         'bot-l': ' ', 'bot-m': ' ', 'bot-r': ' '}

def print_board(param):
    print(param['top-l']+'|'+param['top-m']+'|'+param['top-r'])
    print('-+-+-')
    print(param['mid-l']+'|'+param['mid-m']+'|'+param['mid-r'])
    print('-+-+-')
    print(param['bot-l']+'|'+param['bot-m']+'|'+param['bot-r'])

turn = 'X'
for i in range(0,9):
    print_board(board)
    inp = input('Where would you like your move to be: ')
    if inp == '':
        break
    if board[inp] == ' ':
        board[inp] = turn
    else:
        print('Please enter another place!')
        continue
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'