print("\n\033[34m<< CALCULATE YOUR PROFIT >>\033[0;0m")
print(
    "\nIf you want to calculate your profit, put this informations *USING DOLLAR >>\n")


def profit():
    cost_price = float(input("─ Cost price: \n"))
    sell_price = float(input("─ Sell price: \n"))
    inventory = float(input("─ Inventory: \n"))

    ask = input(
        f'\n\033[32mNow I can calculate the profit, but if you want to calculate the profit of a part of you inventory type [y] or [n]: \033[0;0m')
    if ask == 'n':
        profit = (inventory * sell_price) - (inventory * cost_price)
        print(f'\n\033[34m─ This is your profit: {profit} \033[0;0m')
    elif ask == 'y':
        part_inventory = float(
            input("\nPut here the part of your inventory: \n"))
        profit = (part_inventory * sell_price) - (part_inventory * cost_price)
        print(f'\n\033[34m─ This is your profit: {profit} \033[0;0m')
    else:
        print("\n\033[31mINVALID COMMAND\033[0;0m")


profit()


def restart():
    restart = input(
        "\nIf you want to calculate the profit again type [y] or [n]: ")
    if restart == 'y':
        profit()
    elif restart == 'n':
        exit()
    else:
        print("\n\033[31mINVALID COMMAND\033[0;0m")
        restart()


restart()
