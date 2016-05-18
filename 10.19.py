import random
nballs = eval(input("Enter the number of balls to drop: "))
nslots = eval(input("Enter the number of slots in the bean machine: "))
balls = []
slots = []
path = ""
for h in range(0,nballs):
    balls.append("")
for i in range(0, nslots):
    slots.append(0)
for j in range(0,nballs):
    for k in range(0, nslots):
        x = random.randint(1,2)
        if x == 1:
            path += "L"
        if x == 2:
            path += "R"
    balls[j] = path
    path = ""
for f in range(0,nballs):
    path = list(balls[f])
    slots[path.count("R")] += 1
print(" ")
path = ""
for x in range(0,nballs):
    path = balls[x]
    print(path)
buildup = ""
count = nballs
while count > 0:
    if count in slots:
        for a in range(0, nslots):
            if count <= slots[a]:
                print("0", end = "")
                slots[a]
            else:
                print(" ",end = "")
        print("")
        count -= 1
    elif count not in slots:
        count -=1
        print("")
