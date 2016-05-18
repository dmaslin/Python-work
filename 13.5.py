f = input("Enter a file name: ")

d = input("Enter the string to be replaced: ")

replacement = input("Enter the string to replace the old string: ")

fin = open(f, "r")
s = fin.read().split()
print(s)
for j in range(len(s)):
    if s[j] == d:
        s[j] = replacement      
s = " ".join(s)
fin.close()
fout = open(f, "w")
fout.write(s)
fout.close()
print("Done")
