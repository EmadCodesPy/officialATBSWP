import random

guess = ''
while guess.lower() not in ('heads', 'tails'):
    guess = input('Guess the coin toss! Either heads or tails: ')

toss = random.choice(['heads', 'tails'])

if toss == guess.lower():
    print('You\'ve got it!')
else:
    guess = input('Nope! Guess again: ')
    toss = random.choice(['heads', 'tails'])
    if toss == guess.lower():
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')