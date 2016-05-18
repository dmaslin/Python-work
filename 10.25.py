import random
suit = []
for i in range(0,13):
    suit.append(i+1)
picks = [0, 0, 0, 0]
picksum = []
for a in range(0,13):
    picks[0] = a +1
    for b in range(0,13):
        picks[1] = b +1
        for c in range(0,13):
            picks[2] = c +1
            for d in range(0,13):
                picks[3] = d +1
                picksum.append(sum(picks))
print("The number of combonations that yield 24 is "+ str(picksum.count(24)))
                
