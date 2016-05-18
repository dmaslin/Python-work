def isConsecutiveFour(values):
    for row in range(len(values)):
        for column in range(len(values[0])):
            if row <= (len(values) - 4) and column <= (len(values[0])-4):
                if values[row][column] == values[row + 1][column + 1]  and values[row+1][column +1 ] == values[row + 2][column + 2]  and values[row+2][column + 2] == values[row+3][column + 3]:
                    return True
                elif values[row][column] == values[row][column +1] and values[row][column+1] == values[row][column +2] and values[row][column+2] == values[row][column +3]:
                    return True
                if values[row][column] == values[row+1][column]  and values[row+1][column] == values[row+2][column]  and values[row+2][column] == values[row+3][column]:
                    return True
            elif row <= (len(values) - 4):
                if values[row][column] == values[row+1][column]  and values[row+1][column] == values[row+2][column]  and values[row+2][column] == values[row+3][column]:
                    return True
            elif row >= (len(values) - 4) and column <= (len(values[0]) - 4):
                    if values[row][column] == values[row][column +1] and values[row][column+1] == values[row][column +2] and values[row][column+2] == values[row][column +3]:
                        return True
                    elif values[row][column] == values[row - 1][column + 1]  and values[row-1][column +1 ] == values[row - 2][column + 2]  and values[row-2][column + 2] == values[row-3][column + 3]:
                        return True
    return False

n = eval(input("Enter the number of rows the minimum being 6: "))
print("Please use equal lengths for each row")
values = []
for i in range(n):
    values.append([])
    print("Enter row "+str(i), end = "")
    s = input(": ")
    s = s.split(" ")
    for j in range(len(s)):
        values[i].append(eval(s[j]))
print(isConsecutiveFour(values))


                    
