def isSorted(list1):
    count = 1
    for i in range(1,len(list1)):
        if list1[i] >= list1[i-1]:
            count +=1
    if count == len(list1):
        return True
    else:
        return False
list1 = input('Enter list: ')
list1 = list1.split(" ")
for i in range(0,len(list1)):
    list1[i] = int(list1[i])
ocd = isSorted(list1)
if ocd == True:
    print("The list is already sorted")
elif ocd == False:
    print("The list is not sorted")
