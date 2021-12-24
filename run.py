import turtles
import time

roster = []

class Player:
    def __init__(self,name,color,bet):
        self.name = name
        self.color = color
        self.bet = bet

while True:
    players = input('How many players are playing: ')
    if not players.isdigit():
        print('please enter a number in range of 1 through 10 please')
    else:
        break

spectrum = ['red','blue','green','yellow']

print('place your bets on the winner of the race')
count = 0
valid_checker = 0

while True:
    if count < int(players):
        print(f'player {count+1} please enter')
        name = input('What is your name: ').lower()
        valid_checker += 1
        color = input('What color do you have red, blue, green, or yellow: ').lower()
        if color not in spectrum:
            print('please enter a valid color')
            continue
        else:
            valid_checker += 1
        bet = input("How many drinks or shots are you betting: ").lower().split()
        if len(bet) < 2 or len(bet) > 2:
            continue
        elif bet[0].isdigit() and bet[1] == 'shots' or bet[1] == 'drinks':
            valid_checker += 1
        else:
            print('please enter a valid bet')
    else:
        break
    if valid_checker == 3:
        p = Player(name,color,bet)
        roster.append(p)

        count += 1
    valid_checker = 0

b = turtles.Board('red')

b.start_position()


winner = b.move_turtles()
for r in roster:
    if r.color == winner.color()[0]:
        print(f'{r.name} is the winner you may now give your bet of {r.bet[0]}, {r.bet[1]} out now')
        break
b.close_window()
print(winner.color()[0])
time.sleep(5)