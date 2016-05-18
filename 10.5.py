list1 = input('Enter ten numbers: ')
list1 = list1.split(" ")

list2 = []
for i in range(0,len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
print("The distinct numbers are: ", end = "")
for f in range(0, len(list2)):
    print(list2[f], end = " ")
