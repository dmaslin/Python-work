def countLetters(line, counts):
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1
vowels = {"a", "e", "i", "o", "u"}

f = input("Enter a filename: ").strip()

infile = open(f, "r")
v = 0
c = 0
counts = 26 * [0] # Create and initialize counts
for line in infile:
    countLetters(line.lower(), counts)
infile.close()
for i in range(len(counts)):
    char = chr(97+i)
    if char in vowels:
        v += counts[i]
    elif char not in vowels:
        c += counts[i]

print("The number of vowels is "+str(v))
print("The number of consonants is "+str(c))


