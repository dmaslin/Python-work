scores = input('Enter the scores: ')
scores = scores.split(" ")
for x in range(0,len(scores)):
    scores[x] = int(scores[x])
for i in range(0,len(scores)):
    best = max(scores)
    if best - 10 <= scores[i]:
        print("Student "+str(i+1)+" had a score of "+str(scores[i])+" and their grade is an A")
    elif best - 20 <= scores[i]:
        print("Student "+str(i+1)+" had a score of "+str(scores[i])+" and their grade is an B")
    elif best - 30 <= scores[i]:
        print("Student "+str(i+1)+" had a score of "+str(scores[i])+" and their grade is an C")
    elif best - 40 <= scores[i]:
        print("Student "+str(i+1)+" had a score of "+str(scores[i])+" and their grade is an D")
    else:
        print("Student "+str(i+1)+" had a score of "+str(scores[i])+" and their grade is an F")
