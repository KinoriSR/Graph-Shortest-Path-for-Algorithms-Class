from math import inf

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

def Dijkstra_adj_matrix(G,initial):
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

        #check if shorter routes from this node
        for e in range(rowlength):
            weight=G[current][e]
            #update minimum path
            newWeight=weight+dist[current]
            if dist[e]>newWeight and e!=current:
                dist[e]=newWeight
                Path[e]=current
    #format so nodes don't start with 0
    for r in range(rowlength):
        Path[r]+=1
    return Path, dist

print()
print("Test Cases for Dijkstra's Algorithm using an Adjacency Matrix.")
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
Path, dist=Dijkstra_adj_matrix(test_case1,1)
# print(Path)
# print(dist)
start=1
end=8
print('Weight:', dist[end-1],'| Node Sequence:',findPath(Path,start,end))
print('-----------------------------------------')

Path, dist=Dijkstra_adj_matrix(test_case1,7)
# print(Path)
# print(dist)
start=7
end=8
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
Path, dist=Dijkstra_adj_matrix(test_case2,2)
# print(Path)
# print(dist)
start=2
end=8
print('Weight:', dist[end-1],'| Node Sequence:',findPath(Path,start,end))
print('-----------------------------------------')
Path, dist=Dijkstra_adj_matrix(test_case2,12)
# print(Path)
# print(dist)
start=12
end=10
print('Weight:', dist[end-1],'| Node Sequence:',findPath(Path,start,end))
print('-----------------------------------------')

graph=[ [ 0 , 5 , 7 ,inf,inf],
        [ 5 , 0 ,inf, 2 ,10 ],
        [ 7 ,inf, 0 ,inf,inf],
        [inf, 2 ,inf, 0 , 2 ],
        [inf,10 ,inf, 2 , 0 ]]
#print(Dijkstra_adj_matrix(graph))

graph1 = [[0,32,inf,17,inf,inf,inf,inf,inf,inf],
          [32,0,inf,inf,45,inf,inf,inf,inf,inf],
          [inf,inf,0,18,inf,inf,5,inf,inf,inf],
          [17,inf,18,0,10,inf,inf,3,inf,inf],
          [inf,45,inf,10,0,28,inf,inf,25,inf],
          [inf,inf,inf,inf,28,0,inf,inf,inf,6],
          [inf,inf,5,inf,inf,inf,0,59,inf,inf],
          [inf,inf,inf,3,inf,inf,59,0,4,inf],
          [inf,inf,inf,inf,25,inf,inf,4,0,12],
          [inf,inf,inf,inf,inf,6,inf,inf,12,0]]
#inputs are graph and which vertice range (1,largest vertex index)
#print(Dijkstra_adj_matrix(graph1))