
from random import choice, random, sample, randint
from time import time, sleep


def start():

    print("\n------------------------------------------------------------------------------------------")
    print("\nWELCOME TO ROCK-PAPER-SCISSOR GAME\n")
    global name
    name = input("\nPlease put your name: ")

    # /Rock vs paper = paper wins
    # /Rock vs scissor = Rock wins
    # /paper vs scissor = scissor wins.

    print(
        f'\nPlease {name} put "R" for (Rock), "P" for (Paper) or "S" for (Scissor).\n')

    ready = input("Are you ready ? [y] [n]: ")

    if ready == "y":
        pass
    elif ready == "n":
        print("Ok,bye")
        exit()


def play():

    points_player = 0
    points_robot = 0
    tries = 3

    while True:

        grid = ["R", "S", "P"]
        game = choice(grid)
        player = input("\nGO!: ")
        player = player.upper()

        if player == "R" or player == "P" or player == "S":
            pass
        else:
            print("Invalid command")
            try_again = input("Do you want to try again ? [y] [n]:")
            if try_again == "y":
                start()
            elif try_again == "n":
                print("Ok,bye")
                exit()
            else:
                print("Invalid command")
                exit()

        print(game)

        # @ tie

        if player == game:
            points_player -= 0
            points_robot -= 0
            tries -= 1
            print("Tie !")

        #  @ player wins

        elif player == "P" and game == "R" or player == "R" and game == "S" or player == "S" and game == "P":
            points_player += 1
            tries -= 1
            print(f'{name} you won this round !')

        # @ robot wins

        elif game == "P" and player == "R" or game == "R" and player == "S" or game == "S" and player == "P":
            points_robot += 1
            tries -= 1
            print(f'Robot you won this round !')

        if tries == 0:
            print(
                f'THE GAME WAS: {name}, {points_player} X Robot, {points_robot}')
            if points_player > points_robot:
                print('\033[32m' + name + ' YOU WIN !'+'\033[0;0m\n')
            elif points_robot > points_player:
                print('\033[32m' + '>> ROBOT YOU WIN !'+'\033[0;0m\n')
            else:
                print('\033[32m' + '>> THE GAME TIED !'+'\033[0;0m\n')
            break


start()
play()

again = True
while again == True:
    play_again = input("Do you want to play again ? [y] [n]: ")
    if play_again == "y":
        start()
        play()
    elif play_again == "n":
        print("Ok,bye")
        exit()
    else:
        print("Invalid command")
        exit()
