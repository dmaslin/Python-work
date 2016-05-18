import time
import random
def selectionSort(t, data):
    for i in range(len(data)):
        mini = min(data[i:]) #find minimum element
        min_index = data[i:].index(mini) #find index of minimum element
        data[i + min_index] = data[i] #replace element at min_index with first element
        data[i] = mini #replace first element with min element
    return time.time() - t

def bubbleSort(t, list):
    needNextPass = True
    
    k = 1
    while k < len(list) and needNextPass:
        # List may be sorted and next pass not needed
        needNextPass = False
        for i in range(len(list) - k): 
            if list[i] > list[i + 1]:
                # swap list[i] with list[i + 1]
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
          
                needNextPass = True # Next pass still needed
    return time.time() - t

def mergeSort(t, x):
    if len(x) < 2:
        return x
    result = []          # moved!
    mid = int(len(x)/2)
    y = msort2(x[:mid])
    z = msort2(x[mid:])
    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
    result += y
    result += z
    return time.time() - t
def quickSort(t, list):
    quickSortHelper(list, 0, len(list) - 1)
    return time.time() - t

def quickSortHelper(list, first, last):
    if last > first:
        pivotIndex = partition(list, first, last)
        quickSortHelper(list, first, pivotIndex - 1)
        quickSortHelper(list, pivotIndex + 1, last)

# Partition list[first..last] 
def partition(list, first, last):
    pivot = list[first]  # Choose the first element as the pivot
    low = first + 1  # Index for forward search
    high = last  # Index for backward search

    while high > low:
        # Search forward from left
        while low <= high and list[low] <= pivot:
            low += 1

        # Search backward from right
        while low <= high and list[high] > pivot:
            high -= 1

        # Swap two elements in the list
        if high > low:
            list[high], list[low] = list[low], list[high]

    while high > first and list[high] >= pivot:
        high -= 1

    # Swap pivot with list[high]
    if pivot > list[high]:
        list[first] = list[high]
        list[high] = pivot
        return high
    else:
        return first
def heapSort(t, list):
    from heapsortexercise import Heap as h
    for i in list:
        h.add(i)
    for i in list:
        x = h.remove()
        
    return time.time() - t
def radixSort(t, list):
    RADIX = 10
    maxLength = False
    tmp , placement = -1, 1
    while not maxLength:
        maxLength = True
        # declare and initialize buckets
        buckets = [list() for _ in range( RADIX )]
        # split aList between lists
        for  i in aList:
            tmp = i // placement
            if maxLength and tmp > 0:
                maxLength = False
        # empty lists into aList array
        a = 0
        for b in range( RADIX ):
            buck = buckets[b]
            for i in buck:
                aList[a] = i
                a += 1
        # move to next digit
        placement *= RADIX
    return time.time() - t
print("Arraysize   | Selection Sort\tBubble Sort\tMerge Sort\tQuick Sort\tHeap Sort\tRadix Sort")
print("______________________________________________________________________________________________")

a = 50000
b = 100000
c = 150000
d = 200000
e = 250000
f = 300000
size = [a, b, c, d, e, f]
line = []
for i in range(6):
    line.append([])
d = []
for j in range(6):
    print(str(size[j])+ "    |", end = "")
    for i in range(a):
        w = random.randint(-a, a)
        d.append(w)
    random.shuffle(d)
    r = selectionSort(time.time(), d)
    line[j].append(r)
    random.shuffle(d)
    t = time.time()
    line[j].append(bubbleSort(t, d))
    random.shuffle(d)
    t = time.time()
    line[j].append(mergeSort(t, d))
    random.shuffle(data)
    t = time.time()
    line[j].append(quickSort(t, d))
    random.shuffle(d)
    t = time.time()
    line[j].append(heapSort(t, d))
    random.shuffle(d)
    t = time.time()
    line[j].append(radixSort(t, d))
    print(str(size[j])+ "    |", end = "")
    for i in range(len(line[0])):
        print(format(line[j][i], "10.2f"), end = "")
    print("")
