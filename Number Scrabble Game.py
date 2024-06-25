import random
from random import choice
# this game is to choose three numbers which the sum of it equal 15
def winner(p):
    a, b, c, d, e, f, g, h = [1, 5, 9], [1, 6, 8], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 5, 7], [4, 3, 8], [4, 5, 6]
    if ((all(x in p for x in a)) or (all(x in p for x in b)) or (all(x in p for x in c)) or (all(x in p for x in d)) or
        (all(x in p for x in e)) or (all(x in p for x in f)) or (all(x in p for x in g)) or (all(x in p for x in h))):
        # this condition check if this eight numbers in your choice or no
        return True
def draw(p):
    if not winner(p) and len(used) == 9:
        return True
total = 1
turn = 1
p1, p2 = [], []
print("Welcome in Number Scrabble Game.\nThe player that choose 3 numbers which the sum of it = 15 will win")
play_again = 'y'
while play_again == 'y' or play_again == 'ye' or play_again == 'yes':
    game_setting = int(input("Please choose between:\n1- Playing with computer\n2- Playing with another player\n"))
    if game_setting == 1:
        player1 = input("please enter your name: ")
        player2 = "Computer"
        used = []
        while True:
            rem = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in used:
                rem.remove(i)
            if turn == 1:
                spot = int(input(f"{player1}, please choose number from {rem} and not choose from {used} : "))
                if spot in used or spot > 9 or spot < 1:
                    print("Invalid input!! Try again.")
                elif spot not in used:
                    p1.append(spot)
                    used.append(spot)
                    winner(p1)
                    total += 1
                    turn = 2
            elif turn == 2:
                spot = choice(rem)
                print(f"Computer choose {spot}")
                p2.append(spot)
                used.append(spot)
                winner(p2)
                total += 1
                turn = 1
            if winner(p1):
                print(f"{player1} is win")
                break
            if winner(p2):
                print(f"{player2} is win")
                break
            if draw(p1) and draw(p2):
                print("Game Draw!\n")
                break
        print(f"{player1}'s choices{p1}\n{player2}'s choices{p2}")
    elif game_setting == 2:
        player1 = input("please enter player 1 name: ")
        player2 = input("please enter player 2 name: ")
        used = []
        while True:
            rem = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in used:
                rem.remove(i)
            if turn == 1:
                spot = int(input(f"{player1}, please choose number from {rem} and not choose from {used} : "))
                if spot in used or spot > 9 or spot < 1:
                    print("Invalid input!! Try again.")
                elif spot not in used:
                    p1.append(spot)
                    used.append(spot)
                    winner(p1)
                    total += 1
                    turn = 2
            elif turn == 2:
                spot = int(input(f"{player2}, please choose number from {rem} and not choose from {used}: "))
                if spot in used or spot > 9 or spot < 1:
                    print("Invalid input!! Try again.")
                elif spot not in used:
                    p2.append(spot)
                    used.append(spot)
                    winner(p2)
                    total += 1
                    turn = 1
            if winner(p1):
                print(f"{player1} is win")
                break
            if winner(p2):
                print(f"{player2} is win")
                break
            if draw(p1) and draw(p2):
                print("Game Draw!\n")
        print(f"{player1}'s choices{p1}\n{player2}'s choices{p2}\nDo you want to play again? (y/n): ")
        play_again = input()
# Author: YASSIN ALI