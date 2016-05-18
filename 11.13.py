def locateLargest(a):
    large = 0
    largest = [0, 0]
    for r in range(0, len(a)):
        for c in range(0, len(a[0])):
            if a[r][c] > large:
                large = a[r][c]
                largest[0] = r
                largest[1] = c
    return largest
rows = eval(input("Enter the number of rows: "))

num = []
for r in range(rows):
    num.append([])
    s = input("Enter a row: ")
    s = s.split(" ")
    for c in range(len(s)):
        num[r].append(eval(s[c]))
largest = locateLargest(num)
print("The location of the largest element is at ("+str(largest[0])+", "+str(largest[1])+")")
