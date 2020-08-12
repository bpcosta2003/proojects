def ask():
    global numb
    numb = int(input("Please put a number to find your factorial: "))


ask()

if numb < 0:
    print("Invalid number, the number needs to be > than 0.")
    ask()
else:
    pass

k = 1
while numb > 1:
    k *= numb
    numb -= 1
print(k)
