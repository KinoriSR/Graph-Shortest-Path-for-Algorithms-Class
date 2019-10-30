from math import inf
from LinkedList import *

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

def get_min(unvisited,dist):
    weight=inf
    index=-1
    for i in range(len(unvisited)):
        newWeight=dist[unvisited[i]]
        if newWeight<weight:
            weight=newWeight
            index=i
    return index

def findPath(Path,start,end):
    current=end-1
    L=[end]
    while current!=start-1:
        current=Path[current]-1
        L.insert(0,current+1)
    return L

def Dijkstra_LL(G,initial):
    initial-=1
    rowlength=len(G)

    #make Path matrix
    Path=[]
    for l in range(rowlength):
        if l==initial:
            Path.append(initial)
        else:
            Path.append(None)

    #distance to node [node,distance]
    dist=[]
    for k in range(rowlength):
        if k==initial:
            dist.append(0)
        else:
            dist.append(inf)
    #unvisited with tentative distances [node,distance]
    unvisited = []
    for i in range(rowlength):
            unvisited.append(i)
    for q in range(rowlength):

        #get index of min unvisited
        index=get_min(unvisited,dist)
        current=unvisited[index]
        unvisited=unvisited[:index]+unvisited[index+1:]
        #access the current vertex's linked list = LL
        LL=G[current]
        node=LL.head.next
        #check if shorter routes from this node
        while(node!=LL.tail):
            e=node.val[0]
            weight=node.val[1]
            #update minimum path
            newWeight=weight+dist[current]
            if dist[e]>newWeight:
                dist[e]=newWeight
                Path[e]=current
            node=node.next
    #format so nodes don't start with 0
    for r in range(rowlength):
        Path[r]+=1
    return Path, dist


graph=[ [ 0 , 5 , 7 ,inf,inf],
        [ 5 , 0 ,inf, 2 ,10 ],
        [ 7 ,inf, 0 ,inf,inf],
        [inf, 2 ,inf, 0 , 2 ],
        [inf,10 ,inf, 2 , 0 ]]
# graph=graph_translate_to_LL(graph)
# print('********************************')
# start=5
# end=1
# Path, dist=Dijkstra_adj_matrix(graph,start)
# print(Path)
# print(dist)
# print('Weight:', dist[end-1],'| Node Sequence:',findPath(Path,start,end))
# print('********************************')

print()
print("Test Cases for Dijkstra's Algorithm using an Array of Linked Lists.")
print()
test_case1=[[0,inf,inf,29,inf,inf,inf,inf],
            [inf,0,inf,inf,inf,11,11,inf],
            [inf,inf,0,12,inf,5,5,inf],
            [29,inf,12,0,5,inf,13,inf],
            [inf,inf,inf,5,0,inf,7,11],
            [inf,11,5,inf,inf,0,inf,17],
            [inf,11,5,13,7,inf,0,inf],
            [inf,inf,inf,inf,11,17,inf,0]]
print('Test Case 1:')
print('-----------------------------------------')
start=1
end=8
graph=graph_translate_to_LL(test_case1)
Path, dist=Dijkstra_LL(graph,start)
# print(Path)
# print(dist)
print('Weight:', dist[end-1],'| Node Sequence:',findPath(Path,start,end))
print('-----------------------------------------')
start=7
end=8
graph=graph_translate_to_LL(test_case1)
Path, dist=Dijkstra_LL(graph,start)
# print(Path)
# print(dist)
print('Weight:', dist[end-1],'| Node Sequence:',findPath(Path,start,end))
print()

test_case2=[[0,11,14,inf,8,inf,29,28,inf,inf,14,inf],
            [11,0,12,inf,6,inf,inf,inf,inf,inf,inf,inf],
            [14,12,0,18,13,13,inf,inf,25,inf,inf,16],
            [inf,inf,18,0,inf,inf,27,17,9,25,inf,inf],
            [8,6,13,inf,0,inf,inf,inf,inf,inf,inf,22],
            [inf,inf,13,inf,inf,0,inf,15,5,inf,inf,inf],
            [29,inf,inf,27,inf,inf,0,inf,inf,inf,inf,inf],
            [28,inf,inf,17,inf,15,inf,0,5,9,inf,inf],
            [inf,inf,25,9,inf,5,inf,5,0,inf,25,inf],
            [inf,inf,inf,25,inf,inf,inf,9,inf,0,inf,inf],
            [14,inf,inf,inf,inf,inf,inf,inf,25,inf,0,inf],
            [inf,inf,16,inf,22,inf,inf,inf,inf,inf,inf,0]]
print('Test Case 2:')
print('-----------------------------------------')
start=2
end=8
graph=graph_translate_to_LL(test_case2)
Path, dist=Dijkstra_LL(graph,start)
# print(Path)
# print(dist)
print('Weight:', dist[end-1],'| Node Sequence:',findPath(Path,start,end))
print('-----------------------------------------')
start=12
end=10
graph=graph_translate_to_LL(test_case2)
Path, dist=Dijkstra_LL(graph,start)
# print(Path)
# print(dist)
print('Weight:', dist[end-1],'| Node Sequence:',findPath(Path,start,end))
print('-----------------------------------------')