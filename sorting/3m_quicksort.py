import random

def random_quicksort(A,p,r):
    if p < r:
        q = r3m_partition(A,p,r)
        random_quicksort(A,p,q-1)
        random_quicksort(A,q+1,r)

# 3-median random
def r3m_partition(A,p,r):
    lst = []
    for i in range(3):
        lst.append(random.randrange(p,r))
    n = len(lst)
    lst.sort()
    
    if n % 2 == 0:
        m1 = lst[n//2]
        m2 = lst[n//2-1]
        m = (m1 + m2) / 2
    else:
        m = lst[n//2]
        
    A[r],A[m] = A[m],A[r]
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
n = len(arr) - 1 # must n >= 3
random_quicksort(arr,0,n)
print(arr)