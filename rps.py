from random import randint

play = ["Rock", "Paper", "Scissors"]

computer = play[randint(0, 2)]
print('Computer: {}'.format(computer))

player = input("Rock, Paper, Scissros? ")
print('Player: {}'.format(player))
