import math
def parent(i):
    return i//2

def left(i):
    return 2*i + 1

def right(i): 
    return 2*i + 2

def maxHeapify(A,i):
    l = left(i)
    r = right(i)
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        maxHeapify(A,largest)

def minHeapify(A,i):
    l = left(i)
    r = right(i)
    if l < len(A) and A[l] < A[i]:
        lowest = l
    else:
        lowest = i
    if r < len(A) and A[r] < A[lowest]:
        lowest = r
    if lowest != i:
        A[i],A[lowest] = A[lowest],A[i]
        minHeapify(A,lowest)
    
    
def buildMaxHeap(A):
    for i in range((len(A)//2)-1,-1,-1):
        maxHeapify(A,i)

def buildMinHeap(A):
    for i in range((len(A)//2)-1,-1,-1):
        minHeapify(A,i)
A = [16,4,10,14,7,9,3,2,8,1]
C = [4,1,3,2,16,9,10,14,8,7]
#maxHeapify(A,1)
#print("A is",A)
#buildMaxHeap(C)
#print("C max heap",C)
buildMinHeap(C)
print("C min heap",C)



