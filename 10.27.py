def isConsecutiveFour(list1):
    consecutiveNum = 0
    for i in range(1, len(list1)):
        if list1[i] == list1[i-1]:
            consecutiveNum +=1
            if consecutiveNum == 3:
                return True
        else:
            consecutiveNum = 0
    return False


num = input('Enter at least a 4 digit integer: ')

num = list(num)

for x in range(0, len(num)):
    num[x] = int(num[x])

torf = isConsecutiveFour(num)
for y in range(0, len(num)):
    num[y] = str(num[y])
num = "".join(num)
if torf == True:
    print(num +" has four consecutive numbers.")
elif torf == False:
    print(num + " does not have four consecutive numbers")
