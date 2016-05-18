s = input("Enter a string: ")

chars = list(s)
mlength = 0
mindex = 0
for j in range(len(chars) - 2):
    length = 0
    for i in range(j, len(chars)):
        if chars[i] < chars[i+1]:
            length += 1
        else:
            length += 1 #ensures to include the character at i but not i + 1
            break
    if length > mlength:
        mlength = length
        index = j

string = ""
for a in range(mlength):
    string += chars[a]
        


print("Maximum consecutive increasingly ordered substring is " + string)
