num = eval(input("Enter a number between 0 and 511: "))

num = "{0:09b}".format(num)
num = list(num)

coins = []
for row in range(3):
    coins.append([])
    for column in range(3):
        if num[(row*3) + column] == '0':
            coins[row].append("H")
        elif num[(row*3) + column] == '1':
            coins[row].append("T")
print("")
for r in range(3):
    for c in range(3):
        print(coins[r][c], end = " ")
    print("")
