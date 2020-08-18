range_user = int(input("Put the value of the last factorial number: "))
for numb in range(range_user):

    k = 1
    while numb > 1:
        k *= numb
        numb -= 1
    print(k)
