import random
""" Example from Figure 11.6"""
class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val

T = [[] for _ in range(9)] # hash table with chaining
K = [10,22,37,40,52,60,70,72,75] # set key

def h(k):
    a = random.uniform(min(K),max(K))
    b = random.uniform(min(K),max(K))
    p = 101 # p is not random (you choose 1 prime number) and p > m
    return int((((a*k) + b) % p) % len(T))

def h_insert(T,x):
    h1 = h(x.key)


print(h(75))
