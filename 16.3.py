s1 = input("Enter a string for s1: ")
s2 = input("Enter a string for s2: ")
numMatching = 0
index = -1
for i in range(len(s1)-len(s2)):#s1 - s2 is because it won't need to check any further than that
    if s1[i] == s2[0]:
        for x in range(len(s2)):
            if s1[i + x] == s2[x]:
                numMatching +=1
            else:
                break
        if numMatching == len(s2):
            index = i
if index == -1:
    print("S2 is not a substring of s1")
else:
    print("matched at index "+str(index))
