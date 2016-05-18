locker = []
student = []
s = 1
for x in range(0,100):
    locker.append(False)
for y in range(0,100):
    student.append(y)
while s < 100:
    for z in range(s-1,100, s):
        if locker[z] == False:
            locker[z] = True
        elif locker[z] == True:
            locker[z] = False
    s+=1

for i in range(0,100):
    if locker[i] == False:
        print("Locker L"+str(i+1)+" is Closed")
    elif locker[i] == True:
        print("Locker L"+str(i+1)+" is Open")
