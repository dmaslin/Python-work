def sumColumn(m, columnIndex):
        total = 0
        for row in range(len(m)):
            total += eval(m[row][columnIndex])
        print("Sum of the elements for column "+str(columnIndex)+" is "+format(total, ".1f"))
m = []
for i in range(3):
    print("Enter a 3-by-4 row for row "+str(i), end ="")
    s = input(": ")
    m.append([])
    s = s.split(" ")
    for j in range(4):
        m[i].append(s[j])
for i in range(4):
    sumColumn(m, i)
