""" Open Address (Quadratic Prob)  """
class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val

T = [None for _ in range(10)] # hash table

def h(k,i):
    c1 = i
    c2 = i
    return ((k % len(T)) + (c1*i) + (c2*(i**2))) % len(T)

def h_insert(T,x):
    i = 0
    while i != len(T):
        j = h(x.key,i)
        if T[j] == None:
            T[j] = x
            return j
        else:
            i+=1
    else: 
        return "hash table overflow"

def h_search(T,k):
    i = 0
    while i != len(T):
        j = h(k,i)
        if T[j].key == k:
            return T[j].val
        if T[j] == None:
            break
        i = i + 1
    else:
        return None

def h_delete(T,k):
    i = 0
    while i != len(T):
        j = h(k,i)
        if T[j].key == k:
            tmp = T[j]
            T[j] = None
            return tmp
        if T[j] == None:
            break
        i = i + 1
    else:
        return None

def h_display():
    i = 0 
    for x in T:
        if x != None:
            print(i,"--> key =",x.key,", value =",x.val)
        else:
            print(i,"--> key =",None,", value =",None)
        i+=1

node1 = Node(12,23)
node2 = Node(12,24)
node3 = Node(25,100)
node4 = Node(32,150)
h_insert(T,node1)
h_insert(T,node2)
h_insert(T,node3)
h_insert(T,node4)
h_display()
h_delete(T,12)
print()
h_display()