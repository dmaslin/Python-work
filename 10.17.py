def isAnagram(s1, s2):
    s1.sort()
    s2.sort()
    if s1 == s2:
        return True
    else:
        return False
s1 = input("Enter a word: ")
s2 = input("Enter the alleged anaram: ")
l1 = list(s1)
l2 = list(s2)
anagram = isAnagram(l1, l2)
if anagram == True:
    print(s1+" and "+ s2+" are anagrams")
elif anagram == False:
    print(s1+" and "+ s2+" are not anagrams")
