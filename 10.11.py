import random
def shuffle(list1):
    #because i cannot use shuffle, i will use randint function
    list2 = []
    num = len(list1)
    for i in range(0, num):
        x = random.randint(0,len(list1) - 1)
        list2.append(list1[x])
        list1.pop(x)
    return list2
list1 = input('Enter numbers: ')
list1 = list1.split(" ")
list1 = shuffle(list1)
for i in range(0,len(list1)):
    print(list1[i], end = " ")
        
