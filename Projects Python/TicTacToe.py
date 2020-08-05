
# / começo parte 1

print("\nHey! Ready to play Tic-tac-toe?")
print("\nYou can play this game inviting your friend to play with you using this device, have fun! \n")
print("\nHere is your grid:\n")

game = {
    "A1": " ", "A2": " ", "A3": " ",
    "B1": " ", "B2": " ", "B3": " ",
    "C1": " ", "C2": " ", "C3": " "
}
print("A1|A2|A3\nB1|B2|B3\nC1|C2|C3\n")

# / variaveis parte 2

x = "X"
o = "O"

moves = 0

player = 1

p1 = input("Please put here the name of Player 1: ")
p2 = input("Please put here the name of Player 2: ")

# / possibilidades


def possibility():
    # / possibilidades de vitória do player 1 na horizontal
    if game["A1"] == "X" and game["A2"] == "X" and game["A3"] == "X":
        print(f'{p1} WON THE GAME !')
        exit()
        return 1
    elif game["B1"] == "X" and game["B2"] == "X" and game["B3"] == "X":
        print(f'{p1} WON THE GAME !')
        exit()
        return 1
    elif game["C1"] == "X" and game["C2"] == "X" and game["C3"] == "X":
        print(f'{p1} WON THE GAME !')
        exit()
        return 1
    # / possibilidades de vitória do player 1 na diagonal
    if game["A1"] == "X" and game["B2"] == "X" and game["C3"] == "X":
        print(f'{p1} WON THE GAME !')
        exit()
        return 1
    elif game["A3"] == "X" and game["B2"] == "X" and game["C1"] == "X":
        print(f'{p1} WON THE GAME !')
        exit()
        return 1
    # / possibilidades de vitória do player 1 na vertical
    if game["A1"] == "X" and game["B1"] == "X" and game["C1"] == "X":
        print(f'{p1} WON THE GAME !')
        exit()
        return 1
    elif game["A2"] == "X" and game["B2"] == "X" and game["C2"] == "X":
        print(f'{p1} WON THE GAME !')
        exit()
        return 1
    elif game["A3"] == "X" and game["B3"] == "X" and game["C3"] == "X":
        print(f'{p1} WON THE GAME !')
        exit()
        return 1
    # / possibilidades de vitória do player 2 na horizontal
    if game["A1"] == "O" and game["A2"] == "O" and game["A3"] == "O":
        print(f'{p2} WON THE GAME !')
        exit()
        return 1
    elif game["B1"] == "O" and game["B2"] == "O" and game["B3"] == "O":
        print(f'{p2} WON THE GAME !')
        exit()
        return 1
    elif game["C1"] == "O" and game["C2"] == "O" and game["C3"] == "O":
        print(f'{p2} WON THE GAME !')
        exit()
        return 1
    # / possibilidades de vitória do player 1 na diagonal
    if game["A1"] == "O" and game["B2"] == "O" and game["C3"] == "O":
        print(f'{p2} WON THE GAME !')
        exit()
        return 1
    elif game["A3"] == "O" and game["B2"] == "O" and game["C1"] == "O":
        print(f'{p2} WON THE GAME !')
        exit()
        return 1
    # / possibilidades de vitória do player 1 na vertical
    if game["A1"] == "O" and game["B1"] == "O" and game["C1"] == "O":
        print(f'{p2} WON THE GAME !')
        exit()
        return 1
    elif game["A2"] == "O" and game["B2"] == "O" and game["C2"] == "O":
        print(f'{p2} WON THE GAME !')
        exit()
        return 1
    elif game["A3"] == "O" and game["B3"] == "O" and game["C3"] == "O":
        print(f'{p2} WON THE GAME !')
        exit()
        return 1
    return 0


# / loop parte 3

while True:
    print("\n|"+game["A1"]+"|"+game["A2"]+"|"+game["A3"]+"|")
    print("|"+game["B1"]+"|"+game["B2"]+"|"+game["B3"]+"|")
    print("|"+game["C1"]+"|"+game["C2"]+"|"+game["C3"]+"|")
    total_possibilities = possibility()
    if moves == 9:
        break
    while True:
        if player == 1:
            askp1 = input(f'\n{p1} please select the position in the grid: ')
            if askp1.upper() in game and game[askp1.upper()] == " ":
                game[askp1.upper()] = "X"
                player = 2
                break
            else:
                print("invalid command, try again")
                continue
        else:
            askp2 = input(f'\n{p2} please select the position in the grid: ')
            if askp2.upper() in game and game[askp2.upper()] == " ":
                game[askp2.upper()] = "O"
                player = 1
                break
            else:
                print("invalid command, try again")
                continue
    moves += 1
