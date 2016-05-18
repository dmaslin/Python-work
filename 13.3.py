f = input("Enter a fillename: ")

fin = open(f, "r")

s = fin.read().split()
print("There are "+str(len(s))+" scores")
t = 0
for i in range(len(s)):
    t += eval(s[i])
print("The total is "+str(t))
print("The average is "+ str(t / len(s)))
