import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def draw_board(board):
    cls()
    print('-------------')
    for i in range(3):
        print(f'| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |')
        print('-------------')

board = list(range(10))
draw_board(board)
print()