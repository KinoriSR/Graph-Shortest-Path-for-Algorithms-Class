from math import inf
import math

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

def get_n_nodes(G):
    return 1+((int(math.sqrt(1+8*len(G)))-1)//2)

def Dijkstra_array(G,initial):
    initial-=1
    #find number of nodes
    rowlength=get_n_nodes(G) 

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
    #traverse
    for q in range(rowlength):
        #get index of min unvisited
        index=get_min(unvisited,dist)

        current=unvisited[index]
        unvisited=unvisited[:index]+unvisited[index+1:]

        #check if shorter routes from this node
        for e in range(rowlength):
            if e!=current:
                if e<current:
                    weight=G[((current)*(current-1)//2)+e]
                else:
                    weight=G[((e)*(e-1)//2)+current]

                #update minimum path
                newWeight=weight+dist[current]
                if dist[e]>newWeight:
                    dist[e]=newWeight
                    Path[e]=current
    #format so nodes don't start with 0
    for r in range(rowlength):
        Path[r]+=1
                
    return Path, dist



graph=[ 5,
        7 ,inf,
        inf, 2 ,inf,
        inf,10 ,inf, 2]
#print(Dijkstra_array(graph,5))

print()
print("Test Cases for Dijkstra's Algorithm using a Lower Triangle Data Structure.")
print()
test_case1=[inf,
            inf,inf,
            29,inf,12,
            inf,inf,inf,5,
            inf,11,5,inf,inf,
            inf,11,5,13,7,inf,
            inf,inf,inf,inf,11,17,inf] #28
print('Test Case 1:')
print('-----------------------------------------')
Path, dist=Dijkstra_array(test_case1,1)
# print(Path)
# print(dist)
start=1
end=8
print('Weight:', dist[end-1],'| Node Sequence:',findPath(Path,start,end))
print('-----------------------------------------')
Path, dist=Dijkstra_array(test_case1,7)
# print(Path)
# print(dist)
start=7
end=8
print('Weight:', dist[end-1],'| Node Sequence:',findPath(Path,start,end))
print()

test_case2=[11,
            14,12,
            inf,inf,18,
            8,6,13,inf,
            inf,inf,13,inf,inf,
            29,inf,inf,27,inf,inf,
            28,inf,inf,17,inf,15,inf,
            inf,inf,25,9,inf,5,inf,5,
            inf,inf,inf,25,inf,inf,inf,9,inf,
            14,inf,inf,inf,inf,inf,inf,inf,25,inf,
            inf,inf,16,inf,22,inf,inf,inf,inf,inf,inf]
print('Test Case 2:')
print('-----------------------------------------')
Path, dist=Dijkstra_array(test_case2,2)
# print(Path)
# print(dist)
start=2
end=8
print('Weight:', dist[end-1],'| Node Sequence:',findPath(Path,start,end))
print('-----------------------------------------')
Path, dist=Dijkstra_array(test_case2,12)
# print(Path)
# print(dist)
start=12
end=10
print('Weight:', dist[end-1],'| Node Sequence:',findPath(Path,start,end))
print('-----------------------------------------')
