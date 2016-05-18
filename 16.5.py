s = input("Enter a series of numbers ending with 0: ").split()

mLength = 0
index = 0
num = 0

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        length = 0
        for x in range(i, len(s)-1):#So that it begins at i and can go through all the way to the end of s
            if s[x] == s[x+1]:
                length +=1
            else:
                length += 1 #So that the last value is counted
                break
        if length > mLength:
            mLength = length
            index = i
            num = s[i]
print("The longest same number sequence starts at index "+str(index)+" with "+str(mLength)+" values of "+str(num))
