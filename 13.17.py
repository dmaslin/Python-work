import urllib.request
f = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Salary.txt")
n = []

for line in f:
    n.append(f.readline().decode().split())

allfaculty = 0
assist = 0
assoc = 0
full = 0
counter = 0
avgall = 0
avgassist = 0
avgassoc = 0
avgfull = 0

for i in range(len(n)):
    if n[i][2] == "assistant":
        assist += eval(n[i][3])
        counter += 1
avgassist = assist / counter
counter = 0
for i in range(len(n)):
    if n[i][2] == "associate":
        assoc += eval(n[i][3])
        counter += 1
avgassoc = assoc / counter
counter = 0
for i in range(len(n)):
    if n[i][2] == "full":
        full += eval(n[i][3])
        counter += 1
avgfull = full / counter

counter = 0
for i in range(len(n)):
    allfaculty += eval(n[i][3])
    counter += 1
avgall = allfaculty / counter

print("The total ammount for assistant professors is $"+format(assist, ".2f")+"\nThe average for assistant professors is $"+format(avgassist, ".2f"))
print("")
print("The total ammount for associate professors is $"+format(assoc, ".2f")+"\nThe average for associate professors is $"+format(avgassoc, ".2f"))
print("")
print("The total ammount for full-time professors is $"+format(full, ".2f")+"\nThe average for full-time professors is $"+format(avgfull, ".2f"))
print("")
print("The total ammount for all professors is $"+format(allfaculty, ".2f")+"\nThe average for all professors is $"+format(avgall, ".2f"))
print("")
