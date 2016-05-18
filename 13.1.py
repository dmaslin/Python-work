f = input("Enter a file name: ")

d = input("Enter the string to be removed: ")

fin = open(f, "r")
s = fin.read().split()
print(s)
for j in range(len(s)):
    if s[j] == d:
        s[j] = ""      
s = " ".join(s)
fin.close()
fout = open(f, "w")
fout.write(s)
fout.close()
print("Done")
