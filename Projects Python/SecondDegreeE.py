from math import sqrt

ask = input("Do you want to do a simple second degree equation ? [s],[n] ")


def start():
    if ask == "s":
        pass
    elif ask == "n":
        exit()
    else:
        print("Invalid command")
        exit()


start()

start_equation = print("Put the variables: ")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))


delta = (b**2) - 4 * a * c

if delta > 0:
    print(f'The Delta value is {delta}.')
    print(f'The true values was:')
    print(f'{((-b+(sqrt(delta)))/(2*a)):.2f}')
    print(f'{((-b-(sqrt(delta)))/(2*a)):.2f}')

elif delta == 0:
    print(f'The Delta value is {delta}.')
    print(f'The true values was:')
    print(f'{((-b+(sqrt(delta)))/(2*a)):.2f}')
    print(f'{((-b-(sqrt(delta)))/(2*a)):.2f}')

elif delta < 0:
    print(f'The Delta value is {delta}.')
    print("Don't have true values")
