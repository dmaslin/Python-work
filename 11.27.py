def sortRows(m):
    result = []
    for row in m:
         result.append(row)
    
    for row in result:
        row.sort()

    return result

l1 = []
print("Enter a 3-by-3 maxtrix row by row:")
for r in range(3):
    l1.append([])
    s = input()
    s = s.split(" ")
    for c in range(3):
        l1[r].append(eval(s[c]))
slist = []
for r in range(3):
    slist.append([])
    for c in range(3):
        slist[r].append(l1[c][r])
slist = sortRows(slist)
print("")
print("The column sorted list is")
for c in range(3):
    for r in range(3):
        print(slist[r][c], end = " ")
    print("")
