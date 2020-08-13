parameter = "Somente os index ímpares serão escritos no terminal deste projeto"
separate_items = parameter.split()
odd_index = separate_items[1::2]

for item in odd_index:
    print(item)
