from math import pow

print('\n\033[34m'+'E = mc²'+'\033[0;0m\n')
print("E: Energia (Joule)\nm: Massa (Quilogramas)\nc: Velocidade da Luz (Metros/Segundo)\n")
print("Para resolver a fórmula, você precisa transformar as unidades de medidas corretamente!\n")
print('\033[34m'+'O valor de "c" já existe: 299.792.458(metros/segundo)'+'\033[0;0m\n')

c = 299792458
massa = float(input("Coloque o valor da massa: "))
E = massa * pow(c, 2)
print(f'\n{massa} quilogramas de massa são {E:.2f} Joules')
