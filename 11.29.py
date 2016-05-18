def equals(m1, m2):
    m1.sort()
    m2.sort()
    for i in range(len(m1)):
        if m1[i] != m2[i]:
            return False
    return True
m1 = []
m2 = []
s = input("Enter m1: ").split(" ")
for x in range(len(s)):
    m1.append(eval(s[x]))
s = input("Enter m2: ").split(" ")
for x in range(len(s)):
    m2.append(eval(s[x]))
identical = equals(m1, m2)

if identical == True:
    print("The two lists are identical")
elif identical == False:
    print("The two lists are not identical")
