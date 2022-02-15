import random
import time
import itertools


row1 = [" "," "," "," "]
row2 = [" "," "," "," "]
row3 = [" "," "," "," "]
comp_choose = [num for num in range(1,10)]# computer options
chosen_already = []
player1 = 'x'
player2 = 'o'
win = False
def check_input():
    # while not win:
    user_input = input('Please choose a number between 1-9: ')
    show_message = False
    while not show_message:
        if user_input.isdigit() and int(user_input) >0 and int(user_input) <10 and int(user_input) not in chosen_already:
            show_message = True
            chosen_already.append(int(user_input))
            # print(comp_choose)
            user_assign(int(user_input))
        else:
            user_input = input('Input error or chosen already, choose a num between 1-9: ')


def user_assign(user_input):
    if user_input <= 3 and user_input and user_input>=1:
        row1[user_input-1] = player1
        comp_choice()
    elif user_input >=4 and user_input <=6:
        row2[user_input-4] = player1
        comp_choice()
    elif user_input >=7 and user_input <=9:
        row3[user_input-7] = player1
        comp_choice()

def comp_choice():
    computer = random.choice(comp_choose)
    if computer not in chosen_already:
        if computer <= 3 and computer >= 1:
            row1[computer - 1] = player2
        elif computer >= 4 and computer <= 6:
            row2[computer - 4] = player2
        elif computer >= 7 and computer <= 9:
            row3[computer - 7] = player2
    else:
        computer =random.choice(comp_choose)
    print(row1[:3])
    print(row2[:3])
    print(row3[:3])


def is_win():
    win = False
    while not win:
        # row1_win = set(row1)
        # row2_win = set(row2)
        # row3_win = set(row3)
        if row1[0] == player1 and row1[1] == player1 and row1[2] == player1 or row2[0] == player1 and row2[1] == player1 and row2[2] == player1 or row3[0] == player1 and row3[1] == player1 and row3[2] == player1:
            print(f'Player 1 ({player1}) is the winner!!')
            win = True
            break
        elif (row1[0] == player1 and row2[0] == player1 and row3[0] == player1) or (row1[1] == player1 and row2[1] == player1 and row3[1] == player1) or (row1[2] == player1 and row2[2] == player1 and row3[2] == player1):
            print(f'Player 1 ({player1}) is the winner!!')
            win = True
            break
        elif (row1[0] == player1 and row2[0]==player1 and row3[0] == player1) or (row1[1] == player1 and row2[1]==player1 and row3[1] == player1) or (row1[2] == player1 and row2[2]==player1 and row3[2] == player1):
            print(f'Player 1 ({player1}) is the winner!!')
            win = True
            break
        elif (row1[0] == player1 and row2[1]==player1 and row3[2] == player1) or (row1[2] == player1 and row2[1]==player1 and row3[0] == player1):
            print(f'Player 1 ({player1}) is the winner!!')
            win = True
            break
        elif row1[0] == player1 and row1[1] == player1 and row1[2] == player1 or row2[0] == player1 and row2[1] == player1 and row2[2] == player1 or row3[0] == player1 and row3[1] == player1 and row3[2] == player1:
            print(f'Player 2 ({player2}) is the winner!!')
            win = True
            break
        elif (row1[0] == player2 and row2[0]==player2 and row3[0] == player2) or (row1[1] == player2 and row2[1]==player2 and row3[1] == player2) or (row1[2] == player2 and row2[2]==player2 and row3[2] == player2):
            print(f'Player 2 ({player2}) is the winner!!')
            win = True
            break
        elif (row1[0] == player2 and row2[1] == player2 and row3[2] == player2) or (row1[2] == player2 and row2[1] == player2 and row3[0] == player2):
            print(f'Player 2 ({player2}) is the winner!!')
            win =True
            break
        else:
            check_input()

# while set(row1) == [player1] *3 or set(row2) == [player1] *3 or set(row3) == [player1] *3 or set(row1) == [player3] *3 or set(row2) == [player3] *3 or set(row3) == [player3] *3:

check_input()
is_win()
# print('Tie')
