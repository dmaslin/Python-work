def count(s):
    num = []
    numCounted = []
    for i in range(0,10):
        if str(i) in s:
            num.append(i)
            numCounted.append(s.count(str(i)))
    return num, numCounted
s = input("Enter a string: ")

num, counted = count(s)
for i in range(0, len(num)):
    if counted[i] == 1:
        print(str(num[i])+ " occurs "+str(counted[i])+" time.")
    elif counted[i] > 1:
        print(str(num[i])+ " occurs "+str(counted[i])+" times.")
        
