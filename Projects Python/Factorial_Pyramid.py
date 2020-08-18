range_user = int(input("\nPut the value of the last factorial number: "))
if range_user < 0:
    print("INVALID NUMBER")
    exit()

for numb in range(1, range_user):

    k = 1
    while numb > 1:
        k *= numb
        numb -= 1
    print(k)
