def ins_sort(B):
    for i in range(1,len(B)):
        up = B[i]
        j = i-1
        while j>=0 and B[j] > up:
            B[j+1] = B[j]
        B[j+1] = up
    return B

def b_sort(A):
    n = len(A)
    B = []
    for i in range(n):
        B.append([])

    for j in A:
        index_b = int(n*j)
        B[index_b].append(j)

    for i in range(n):
        B[i] = ins_sort(B[i])

    k=0
    for i in range(n):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k+=1
    return A    

x = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print(b_sort(x))  

