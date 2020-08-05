# 1
print("Welcome to my number organizer list!\nHere you can type any number you want and at the end\neverything will get organized :D")

continuar = "y"
lista = []


def organizer():
    while continuar == "y":
        to_be_added = str(
            input("\nType any number you want to add into the list to get organized:\n"))
        lista.append(to_be_added)
        decision = input(
            "\nYou want to add a new number? Press 'y' if yes, otherwise just press 'n': \n")
        if decision == "n":
            break

    increasing_decreasing = str(input(
        "It's time to select how do you want your final result. For increasing order press 'i',for decreasing order press 'd':\n"))

    if increasing_decreasing == "i":
        lista.sort()
        print("That's your final list:", lista)
    elif increasing_decreasing == "d":
        lista.reverse()
        print("That's your final list:", lista)


organizer()

# 2
print("««««««««««««««««««««««««««««««««««««««««««««")

print("Informe número a número de uma lista para ordenar.\n")

continuar = "s"
lista = []

while continuar == "s":
    numero = int(input("Digite um número inteiro: "))
    lista.append(numero)
    continuar = input("Deseja continuar? [s] ou [n]: ")
    if continuar == "n":
        break


p = input("Quer organizar sua lista crescente [c] ou decrescente [d]: ")
if p == "c":
    lista.sort()
elif p == "d":
    lista.reverse()

print(lista)

print("««««««««««««««««««««««««««««««««««««««««««««")

# 3
print("Informe número a número de uma lista para ordenar:")

continuar = "s"
lista = []

while continuar == "s":
    numero = int(input("\nDigite um número inteiro\n"))
    lista.append(numero)
    continuar = input("Deseja continuar? [s] ou [n]\n")

print("\nSua lista ficou assim: " + str(lista))

lista2 = []

while len(lista) > 0:
    menor = lista[0]
    posicao = 0
    for index, element in enumerate(lista):
        if menor > element:
            menor = element
            posicao = index
    lista2.append(menor)
    lista.pop(posicao)

print("\nSua lista ordenada: " + str(lista2))

print("««««««««««««««««««««««««««««««««««««««««««««")

# 4
lista = []
flag = False

for x in range(8):

    tamanho = len(lista)

    n = int(input("Digite um número inteiro: "))

    if(tamanho > 0):

        for y in range(tamanho):

            if (n <= lista[y]):

                lista.insert(y, n)

                flag = True

                break

    elif((x == 0) or (flag == False)):

        lista.append(n)

    else:

        flag = False

print(lista)

print("««««««««««««««««««««««««««««««««««««««««««««")
