n = eval(input("Enter the total number of banks: "))
limit = eval(input("Enter the minimum total assets for keeping a bank safe: "))

bank = []
print("Please enter the following information for each bank in this order. Assets, number of banks that it borrowed from, bank id number, ammount borrowed. Repeat the last two for as many banks as needed.")
for row in range(n):
    bank.append([])
    print("Enter the info for bank "+str(row), end = "")
    s = input(": ")
    s = s.split(" ")
    for column in range(len(s)):
        bank[row].append(eval(s[column]))
assets = []
safe = []
for row in range(n):
    assets.append(bank[row][0])
    safe.append(True)
unsafe = []
lenOldUnsafe = len(unsafe)
for row in range(n):
    total = 0
    total += assets[row]
    for column in range(bank[row][1]):
        amt = 3
        bnum = 2
        if safe[bank[row][(bnum + (2*column))]] == True:
            total += bank[row][(amt + (2*column))]
        elif safe[bank[row][(bnum + (2*column))]] == False:
            total += 0
    if total < limit:
        safe[row] = False
        if row not in unsafe:
            unsafe.append(row)
lenNewUnsafe = len(unsafe)
while lenOldUnsafe < lenNewUnsafe:
    lenOldUnsafe = lenNewUnsafe
    for row in range(n):
        total = 0
        total += assets[row]
        for column in range(bank[row][1]):
            amt = 3
            bnum = 2
            if safe[bank[row][(bnum + (2*column))]] == True:
                total += bank[row][(amt + (2*column))]
            elif safe[bank[row][(bnum + (2*column))]] == False:
                total += 0
        if total < limit:
            safe[row] = False
            if row not in unsafe:
                unsafe.append(row)
    lenNewUnsafe = len(unsafe)
print("The unsafe banks are ", end = "")
for i in range(len(unsafe)):
    print(unsafe[i],end = " ")
