import random

def random_quicksort(A,p,r):
    if p < r:
        q = random_partition(A,p,r)
        random_quicksort(A,p,q-1)
        random_quicksort(A,q+1,r)

def random_partition(A,p,r):
    i = random.randrange(p,r)
    A[r],A[i] = A[i],A[r]
    return partition(A,p,r)

def partition(A,p,r):
    pivot = p
    i = p + 1
    for j in range(p+1,r+1):
        if A[j] <= A[pivot]:
            A[i],A[j] = A[j],A[i]
            i = i + 1
    A[pivot],A[i-1] = A[i-1],A[pivot]
    pivot = i-1
    return pivot

arr = [10, 7, 8, 9, 1, 5] 
arr1 = [10, 80, 30, 90, 40, 50, 70]
n = len(arr1) - 1
random_quicksort(arr1,0,n)
print(arr1)