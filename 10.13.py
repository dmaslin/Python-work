def eliminateDuplicates(list1):
    maximum = max(list1)
    minimum = min(list1)
    for i in range(minimum, maximum + 1):
        numCounted = list1.count(i)
        if numCounted > 1:
            for x in range(0,numCounted - 1):
                list1.remove(i)
    return list1
list1 = input('Enter ten numbers: ')
list1 = list1.split(" ")
for j in range(0, len(list1)):
    list1[j] = int(list1[j])
list1 = eliminateDuplicates(list1)
print("The distinct numbers are: ", end = "")
for i in range(0, len(list1)):
    print(list1[i],end = " ")
