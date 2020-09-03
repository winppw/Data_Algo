def c_sort(A,expo):
    n = len(A)
    output = [0] * (n)
    count = [0] * (10) # k=10
    for i in range(0,n):
        index = int(A[i]/expo)
        count[(index)%10] = count[(index)%10] + 1

    for i in range(1,10):
        count[i] += count[i-1]

    for i in range(n-1,-1,-1):
        index = int(A[i]/expo)
        output[count[(index)%10]-1] = A[i]
        count[(index)%10] -= 1

    for i in range(0,n):
        A[i] = output[i]    

def r_sort(A):
    max_e = max(A)
    expo = 1
    while max_e/expo > 0:
        c_sort(A,expo)
        expo *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 66]
r_sort(arr)
print(arr)

    
