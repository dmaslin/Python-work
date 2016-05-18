from heapsortexercise import Heap

def heapSort(list):
    heap = Heap() # Create a Heap 

    # Add elements to the heap
    for v in list:
        heap.add(v)

    # Remove elements from the heap
    for i in range(len(list)): 
        list[i] = heap.remove()
  
def main():
    s = input("Enter a numeric list: ").split()
    x = []
    for i in range(len(s)):
        x.append(eval(s[i]))
    heapSort(x)
    for v in x:
        print(str(v) + " ", end = " ")

main()
