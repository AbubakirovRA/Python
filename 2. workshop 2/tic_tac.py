import os
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_board(board):
    cls()
    print('-------------')
    for i in range(3):
        print(f'| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |')
        print('-------------')

def request_number(title):
    while True:
        try:
            num = int(input(title))
            if 0 < num < 10:
                return num
        except ValueError:
            print('Your entered wrong! One more!)')

def init_game():
    print('---------------------')
    print('______HI, THERE!____')
    print('This is TIC-TAC Game!')
    print('---------------------')
    print()
    print('______RULES__________')
    print('The first move is made by the player who plays for X\nThe turn order is determined by tossing a coin.')
    print()
    import random
    first_step = random.randint(1 ,2)
    while True:
        player1, player2 = input('Enter name Player1: '), input('Enter name Player2: ')
        if player1 != player2:
            if player1 != '' and player2 != '':
                return player1, player2, first_step
        print('Wrong enter!(Empty or same names')

print (init_game())
board = list(range(10))
draw_board(board)
print(request_number('enter integer from 0 to 9 '))

