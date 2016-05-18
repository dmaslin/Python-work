import random
list1 = []
for i in range(0, 1000):
    list1.append(random.randint(0,9))
for x in range(0,10):
    if list1.count(x) > 1:
        print(str(x)+" occurs "+str(list1.count(x))+" times")
    else:
        print(str(x)+" occurs "+str(list1.count(x))+" time")
