def tradutor(phrase):
    tradução = " "

    for letra in phrase:

        if letra in "aA":
            tradução = tradução + "k"
        elif letra in "bB":
            tradução = tradução + "t"
        elif letra in "cC":
            tradução = tradução + "v"
        elif letra in "dD":
            tradução = tradução + "l"
        elif letra in "eE":
            tradução = tradução + "p"
        elif letra in "fF":
            tradução = tradução + "&"
        elif letra in "gG":
            tradução = tradução + "!"
        elif letra in "hH":
            tradução = tradução + "¬"
        elif letra in "iI":
            tradução = tradução + "§"
        elif letra in "jJ":
            tradução = tradução + "z"
        elif letra in "kK":
            tradução = tradução + "g"
        elif letra in "lL":
            tradução = tradução + "b"
        elif letra in "mM":
            tradução = tradução + "n"
        elif letra in "nN":
            tradução = tradução + "m"
        elif letra in "oO":
            tradução = tradução + "$"
        elif letra in "pP":
            tradução = tradução + "%"
        elif letra in "qQ":
            tradução = tradução + "/"
        elif letra in "rR":
            tradução = tradução + "y"
        elif letra in "sS":
            tradução = tradução + "+"
        elif letra in "tT":
            tradução = tradução + "|"
        elif letra in "uU":
            tradução = tradução + "f"
        elif letra in "vV":
            tradução = tradução + "w"
        elif letra in "wW":
            tradução = tradução + "r"
        elif letra in "xX":
            tradução = tradução + "q"
        elif letra in "yY":
            tradução = tradução + "-"
        elif letra in "zZ":
            tradução = tradução + "ç"
        else:
            tradução = tradução + letra
    return tradução


print(tradutor(input("O que voce quer criptografar: ")))


def tradutor1(phrase):
    tradução = " "

    for letra in phrase:

        if letra in "k":
            tradução = tradução + "a"
        elif letra in "t":
            tradução = tradução + "b"
        elif letra in "v":
            tradução = tradução + "c"
        elif letra in "l":
            tradução = tradução + "d"
        elif letra in "p":
            tradução = tradução + "e"
        elif letra in "&":
            tradução = tradução + "f"
        elif letra in "!":
            tradução = tradução + "g"
        elif letra in "¬":
            tradução = tradução + "h"
        elif letra in "§":
            tradução = tradução + "i"
        elif letra in "z":
            tradução = tradução + "j"
        elif letra in "g":
            tradução = tradução + "k"
        elif letra in "b":
            tradução = tradução + "l"
        elif letra in "n":
            tradução = tradução + "m"
        elif letra in "m":
            tradução = tradução + "n"
        elif letra in "$":
            tradução = tradução + "o"
        elif letra in "%":
            tradução = tradução + "p"
        elif letra in "/":
            tradução = tradução + "q"
        elif letra in "y":
            tradução = tradução + "r"
        elif letra in "+":
            tradução = tradução + "s"
        elif letra in "|":
            tradução = tradução + "t"
        elif letra in "f":
            tradução = tradução + "u"
        elif letra in "w":
            tradução = tradução + "v"
        elif letra in "r":
            tradução = tradução + "w"
        elif letra in "q":
            tradução = tradução + "x"
        elif letra in "-":
            tradução = tradução + "y"
        elif letra in "ç":
            tradução = tradução + "z"
        else:
            tradução = tradução + letra
    return tradução


print(tradutor1(input("O que voce quer descriptografar: ")))
