import random


guess = ''
while guess not in ('heads', 'tails'):
    guess = input('Guess the coin toss!, Enter heads or tails: ')
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 0 and guess == 'heads' or toss == 1 and guess == 'tails':
    print('You got it!')
else:
    guess = input('Nope! Guess again! ')
    if toss == 0 and guess == 'heads' or toss == 1 and guess == 'tails':
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

