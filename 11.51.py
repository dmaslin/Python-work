student = []

s = input("Enter students' name and scores: ").split()
x = len(s)
x = x/2
x = int(x)
for i in range(x):
    student.append([])
    for j in range(2):
        student[i].append(int(s[(2*i)+1]))
        student[i].append(s[2*i])
student.sort()

for i in range(len(student)):
    print(student[i][1] + "\t"+str(student[i][0]))
