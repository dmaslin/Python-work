def addMatrix(a, b):
    c = []
    for row in range(len(a)):
        c.append([])
        for column in range(len(a[0])):
            c[row].append(a[row][column] + b[row][column])
    for row in range(len(a)):
        for column in range(len(a[0])):
            print(format(a[row][column], "2.1f"), end = " ")
            if column == 2 and row == 1:
                print("\t"+"+"+"\t", end = "")
            elif column == 2 and row != 1:
                print("\t \t", end = "")
        for column in range(len(b[0])):
            print(format(b[row][column], "2.1f"), end = " ")
            if column == 2 and row == 1:
                print("\t"+"="+"\t", end = "")
            elif column == 2 and row != 1:
                print("\t \t", end = "")
        for column in range(len(c[0])):
            print(format(c[row][column], "3.1f"), end = " ")
            if column == 2:
                print("")
s1 = input("Enter matrix1: ")
s2 = input("Enter matrix2: ")
a = []
b = []
s1 = s1.split(" ")
s2 = s2.split(" ")
for i in range(3):
    a.append([])
    b.append([])
    for j in range(3):
        a[i].append(eval(s1[(3*i)+j]))
        b[i].append(eval(s2[(3*i)+j]))
addMatrix(a, b)
