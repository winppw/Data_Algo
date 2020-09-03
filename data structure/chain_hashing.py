class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val


T = [[] for _ in range(10)] #hash table

def h(x):
    return x % len(T)

def ch_insert(T,x):
    hashvalue = h(x.key)
    T[hashvalue].append(x)

def ch_search(T,k):
    hashvalue = h(k)
    for x in T[hashvalue]:
        if k == x.key:
            return x.val
    return -1

def ch_delete(T,x):
    hashvalue = h(x.key)
    for obj in T[hashvalue]:
        if x.val == obj.val:
            T[hashvalue].remove(obj)
            break

def ch_display(T):
    for i in range(len(T)):
        print(i, end=" ")
        for j in T[i]:
            print("-->", end=" ")
            print(j.val, end=" ")
        print()

ch_insert(T,Node(12,3))
ch_insert(T,Node(13,4))
ch_insert(T,Node(14,7))
ch_insert(T,Node(15,12))
ch_insert(T,Node(16,120))
ch_display(T)
ch_delete(T,Node(16,120))
print()
ch_display(T)