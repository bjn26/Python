import random
import sys
print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print("Enter your move: (r)ock (p)aper (s)cissor or (q)uit")
        Move = input()
        if Move == 'q':
             sys.exit()
        if Move == 'r' or Move == 'p' or Move == 's':
            break
        print('Type one of r, p, s, or q.')

    if Move == 'r':
        print('ROCK versus...')
    elif Move == 'p':
        print('PAPER versus...')
    elif Move == 's':
        print('SCISSORS versus...')

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    if Move == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif Move == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif Move == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif Move == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif Move == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif Move == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif Move == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1