#This is a rock paper scissors game
import random
user_move = input("Enter your move (r/p/s): ").upper()
moves = ['R','P','S']
computer_move = moves[random.randint(0,2)]

if user_move == computer_move:
    print("This round is a TIE")
if user_move == 'R':
    if computer_move == 'P':
        print("You LOST this round")
    else:
        print("You have WON this round")
if user_move == 'P':
    if computer_move == 'S':
        print("You have LOST this round")
    if computer_move == 'R':
        print("You have WON this round")

if user_move == 'S':
    if computer_move == 'R':
        print('You have LOST this round')
    if computer_move == 'P':
        print("You have WON this round")


print(user_move, computer_move)