from random import random

N = 10
while N != 81:
    loss = 0
    for x in range(10000):
        lattice = []  # No points in the lattice are traversed initially
        for i in range(N):
            list = N * [False] 
            lattice.append(list)

        i = (N + 1) // 2
        j = (N + 1) // 2
        lattice[i][j] = True # Starting point
        while i > 0 and i < N - 1 and j > 0 and j < N - 1:   
            if lattice[i][j + 1] and lattice[i][j - 1] and lattice[i - 1][j] and lattice[i + 1][j]:
                loss += 1
                break
                      
            r = random()
            if r < .25 and not lattice[i][j + 1]:
                lattice[i][j + 1] = True # Right
                j += 1      
            elif r < .50 and not lattice[i - 1][j]:
                lattice[i - 1][j] = True # Down
                i -= 1      
            elif r < .75 and not lattice[i][j - 1]:
                lattice[i][j - 1] = True # Left
                j -= 1      
            elif r < 1.00 and not lattice[i + 1][j]:
                lattice[i + 1][j] = True # Up
                i += 1
    chance = (loss /10000)*100
    print("For a lattice size "+str(N)+", the probability of dead-end paths is "+format(chance, ".1f")+"%")
    N += 1
