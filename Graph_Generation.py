from LinkedList import *
from math import inf
import math
from random import randint
import sys

#list of edges and vertex then remove what is visited
N1=Node(val=2)
N2=Node(val=1) 
N1.next=N2
N2.prev=N1
print(sys.getsizeof(Node(val=[1,2])))

# print(N1.next.val)
# print(N2.prev.val)

# L=LinkedList()
# L.head.next=N1
# L.tail.prev=N2
# N2.next=L.tail
# N1.prev=L.head
# node=L.head.next
# while (node!=L.tail):
#     print(node.val)
#     node=node.next

test_case1=[[0,inf,inf,29,inf,inf,inf,inf],
            [inf,0,inf,inf,inf,11,11,inf],
            [inf,inf,0,12,inf,5,5,inf],
            [29,inf,12,0,5,inf,13,inf],
            [inf,inf,inf,5,0,inf,7,11],
            [inf,11,5,inf,inf,0,inf,17],
            [inf,11,5,13,7,inf,0,inf],
            [inf,inf,inf,inf,11,17,inf,0]]

def graph_translate_to_LL(G):
    Graph=[]
    length=len(G)
    for i in range(length):
        L=LinkedList()
        node=L.head
        Graph.append(L)
        for j in range(length):
            value=G[i][j]
            if (value!=inf and value!=0):
                #create node
                new_node=Node(val=[j,value])
                #new_node's previous is node
                new_node.prev=node
                #previous node points to new_node
                node.next=new_node
                #now point to new_node
                node=new_node
        #complete the chain
        node.next=L.tail
        #tail.prev is the added node
        L.tail.prev=new_node
    return Graph

def graph_translate_to_LowTri(G):
    length=len(G)
    Graph=[]
    for i in range(1,length):
        for j in range(i):
            Graph.append(G[i][j])
    return Graph

#Translate to Array of Linked Lists
# Graph=graph_translate_to_LL(test_case1)
# length=len(Graph)
# for k in range(length):
#     node=Graph[k].head.next
#     while (node!=Graph[k].tail):
#         print(node.val, end=' ')
#         node=node.next
#     print()

#Translate to Lower Triangle
# Graph=graph_translate_to_LowTri(test_case1)
# length=1+((int(math.sqrt(1+8*len(Graph)))-1)//2)
# new=0
# for i in range(1,length):
#     print(Graph[new:new+i])
#     new+=i

#generate a random undirected complete graph of size n as adjacency matrix
def Generate_Complete_Graph(n):
    G=[]
    for k in range(n):
        G.append([])
    for i in range(n):
        for j in range(i,n):
            if i!=j:
                num=randint(1,20)
                G[i].append(num)
                G[j].insert(i,num)
            else:
                G[i].append(0)
    return G

#generate random undirected sparse graph of size n as adjacency matrix
def Generate_Sparse_Graph(n):
    G=[]
    for k in range(n):
        G.append([])
    for i in range(n):
        if i<n-1:
            random_index=randint(i+1,n-1)
        for j in range(i,n):
            if i!=j and j==random_index:
                num=randint(1,20)
                G[i].append(num)
                G[j].insert(i,num)
            elif i!=j and j!=random_index:
                num=inf
                G[i].append(num)
                G[j].insert(i,num)
            else:
                G[i].append(0)
    return G

#generate random undirected random graph of size n as adjacency matrix
def Generate_Random_Graph(n):
    G=[]
    for k in range(n):
            G.append([])
    n=n-1
    for i in range(n+1):
        #make list of random numbers
        randoms=[]
        random_index_range=randint(1,n-i+1)
        for r in range(random_index_range):
            randoms.append(randint(1,20))
        #insert the rest as inf or 0
        for s in range(n-i-random_index_range):
            random_index=randint(0,n)
            randoms.insert(random_index,inf)
        #loop through the random list and append and insert in the right places like complete graph
        for j in range(i,n+1):
            if i!=j:
                num=randoms[j-i-1]
                G[i].append(num)
                G[j].insert(i,num)
            else:
                G[i].append(0)            
    return G

# print('-------------')
# n=7
# G=Generate_Complete_Graph(n)
# for i in range(len(G)):
#     print(G[i])

# print('-------------')
# n=10
# G=Generate_Sparse_Graph(n)
# for i in range(len(G)):
#     print(G[i])
