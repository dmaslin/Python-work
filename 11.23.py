
m1 = []
for row in range(6):
    m1.append([])
    for column in range(6):
        if row == 0 and column == 0:
            m1[row].append(1)
        elif row == 0 and column == 2:
            m1[row].append(1)
        elif row == 0 and column == 3:
            m1[row].append(1)
        elif row == 0 and column == 5:
            m1[row].append(1)
        elif row == 1 and column == 1:
            m1[row].append(1)
        elif row == 1 and column == 4:
            m1[row].append(1)
        elif row == 4 and column == 1:
            m1[row].append(1)
        elif row == 4 and column == 4:
            m1[row].append(1)
        elif row == 5 and column == 0:
            m1[row].append(1)
        elif row == 5 and column == 2:
            m1[row].append(1)
        elif row == 5 and column == 3:
            m1[row].append(1)
        elif row == 5 and column == 5:
            m1[row].append(1)
        else:
            m1[row].append(0)

for r in range(6):
    for c in range(6):
        print(m1[r][c], end = " ")
    print("")

m2 = []
print("Change one value from the matrix above")
for r in range(6):
    s = input("Enter the matrix line: ")
    s = s.split(" ")
    m2.append([])
    for c in range(6):
        m2[r].append(eval(s[c]))
changed = []

for r in range(6):
    if sum(m2[r]) % 2 != 0:
        changed.append(r)
for c in range(6):
    total = 0
    for r in range(6):
        total += m2[r][c]
    if total % 2 != 0:
        changed.append(c)
print("You changed a value at "+str(changed[0])+", "+str(changed[1]))
