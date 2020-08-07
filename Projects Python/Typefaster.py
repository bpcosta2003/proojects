from random import choice, randint, random, randrange
from time import time, sleep

print("BEM VINDO AO TYPE FAST, AQUI VOCÊ PODE TREINAR SUA DIGITAÇÃO\n")


def frases():
    print("Selecione a dificuldade para digitação:\n ")
    global possalt
    possalt = input("1.Fácil\n2.Médio\n3.Difícil\n\n")

    if str(possalt) == "1":

        print("Você tem 10 segundos para digitar esta frase:\n")
        print("/////////////////////////////")
        print("|Estou digitando no teclado.|")
        print("/////////////////////////////\n")
    elif str(possalt) == "2":

        print("Você tem 5 segundos para digitar esta frase:\n")
        print("/////////////////////////////")
        print("|Estou digitando no teclado.|")
        print("/////////////////////////////\n")
    elif str(possalt) == "3":

        print("Você tem 3 segundos para digitar esta frase:\n")
        print("/////////////////////////////")
        print("|Estou digitando no teclado.|")
        print("/////////////////////////////\n")
    else:
        print("Comando inválido")
        exit()

    i = input("Está pronto? digite [y] para sim e [n] para não: ")
    print(" ")
    if i == "y":
        pass
    elif i == "n":
        exit()

    for i in range(3, -1, -1):
        print(i)
        sleep(1)

    print("Já!")
    global start
    start = time()
    var = input("DIGITE O MAIS RÁPIDO POSSÍVEL: ")
    if var != "Estou digitando no teclado.":
        y = input(
            "Você digitou a frase de maneira incorreta, tente novamente, digite [v] para voltar: ")
        if y == "v":
            frases()
        else:
            print("Comando inválido")
            exit()
    global end
    end = time()

    print("  ")


frases()


def estp():
    j = input(
        "Está pronto para bater seu record? digite [y] para sim e [n] para não: ")
    if j == "y":
        pass
    elif j == "n":
        exit()
    print(" ")
    for i in range(3, -1, -1):
        print(i)
        sleep(1)
    print("Já!")


estp()


def tempo():
    global start1
    start1 = time()
    var1 = input("TENTE BATER SEU RECORD, DIGITE MAIS RÁPIDO! : ")
    if var1 != "Estou digitando no teclado.":
        y = input(
            "Você digitou a frase de maneira incorreta, tente novamente, digite [v] para voltar: ")
        if y == "v":
            estp()
            tempo()
        else:
            print("Comando inválido")
            exit()
    global end1
    end1 = time()


tempo()


def end_star():
    tempo = round(end - start, 1)
    tempo1 = round(end1 - start1, 1)
    print("\nDados:\n")
    print("Você digitou em", tempo, "segundos na primeira e",
          tempo1, "segundos na segunda.")
    if possalt == "1":
        print("Era para ser em 10 segundos e você fez em", tempo1, ".")
    elif possalt == "2":
        print("Era para ser em 5 segundos e você fez em", tempo1, ".")
    elif possalt == "3":
        print("Era para ser em 3 segundos e você fez em", tempo1, ".")
    else:
        print("Comando inválido")
        exit()

    if tempo == tempo1:
        print("Seu tempo foi igual em ambos.")
    elif tempo < tempo1:
        print("Você não bateu seu record, você fez em", round(
            tempo1 - tempo, 1), "segundos mais devagar.")
    else:
        print("UAU! Você bateu seu record, você fez em", round(
            tempo - tempo1, 1), "segundos mais rápido.")


end_star()
