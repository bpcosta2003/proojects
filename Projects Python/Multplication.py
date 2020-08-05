
from random import randrange as r
from time import time as t


def mult():
    no_questions = int(input('Quantas questões você quer: '))
    max_num = int(input('Maior número para calcular: '))

    score = 0
    answer_list = []

    start = t()
    for q in range(no_questions):
        num1, num2 = r(1, max_num+1), r(1, max_num+1)
        ans = num1 * num2
        u_ans = int(input(f'{num1} X {num2} = '))
        answer_list.append(f'{num1} X {num2} = {ans} você colocou:{u_ans}')
        if u_ans == ans:
            score += 1
        end = t()
    print(
        f'Obrigado por jogar! \nVocê fez {score} de {no_questions} ({round(score/no_questions*100)}%) em {round(end-start,1)} segundos ({round((end-start)/no_questions,1)}seconds/question)')
    for a in answer_list:
        print(a)


def restart():
    rest = input(
        "Quer jogar novamente ? -- digite [y] para sim e [n] para não: ")

    if rest == "y":
        while rest == "y":
            mult()
    elif rest == "n":
        try:
            print("OK")
        except:
            print("SyntaxError")
    else:
        print("INVÁLIDO")
        restart()


mult()
restart()
