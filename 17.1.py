def getPivot(l):
    p = []
    p.append(l[0])#first element
    p.append(l[len(l) - 1]) #last element
    if len(l) %2 == 1:
        x = l[len(l)//2  + 1 =]
        p.append(x) #middle element
        p.sort()#me being lazy in typing the comparison of the three elements
        return p[1]
        

    elif len(l) % 2 == 0:
        x = l[(len(l)//2)]
        p.append(x)
        p.sort()
        return p[1]
def quickSort(list):
    quickSortHelper(list, 0, len(list) - 1)

def quickSortHelper(list, first, last):
    if last > first:
        pivotIndex= partition(list, first, last)
        quickSortHelper(list, first, pivotIndex - 1)
        quickSortHelper(list, pivotIndex + 1, last)

# Partition list[first..last] 
def partition(list, first, last):
    pivot = list[first]  # Choose the first element as the pivot
    low = first + 1  # Index for forward search
    high = last  # Index for backward search
    while high > low:
        
        while low <= high and list[high]>pivot:
            high -= 1
            
        # Search forward from left
        while low <= high and list[low] <= pivot:
            low += 1
        
        # Swap two elements in the list
        if high > low:
            list[high], list[low] = list[low], list[high]

    # Swap pivot with list[high]
    if pivot > list[high]:
        list[first] = list[high]
        list[high] = pivot
        return high
    else:
        return first 
# A test function 
def main():
    list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    quickSort(list)
    for v in list:
        print(str(v) + " ", end = "")

main()
