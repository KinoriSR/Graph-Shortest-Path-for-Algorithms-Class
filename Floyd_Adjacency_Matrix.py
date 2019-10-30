from math import inf
import math

def findPath2(Path,s,e):
    print(s,end=',')
    findPathHelp(Path,s-1,e-1)
    print(e)
#From the textbook
def findPathHelp(Path,s,e):
    if Path[s][e]!=-1:
        findPathHelp(Path,s,Path[s][e])
        print(Path[s][e]+1,end=',')
        findPathHelp(Path,Path[s][e],e)

def Floyd_adj_matrix(G):
    rowlength=len(G)
    Path=[]
    L=[]
    #Make Path
    for x in range(rowlength):
        Path.append([])
        for y in range(rowlength):
            Path[x].append(-1)

    for k in range(rowlength):
        for i in range(rowlength):
            for j in range(rowlength):
                newWeight=G[i][k]+G[k][j]
                if newWeight<G[i][j]:
                    Path[i][j]=k
                    G[i][j]=newWeight
    
    return Path, G



graph=[ [ 0 , 5 , 7 ,inf,inf],
        [ 5 , 0 ,inf, 2 ,10 ],
        [ 7 ,inf, 0 ,inf,inf],
        [inf, 2 ,inf, 0 , 2 ],
        [inf,10 ,inf, 2 , 0 ]]
# print('********************************')
# Path,Graph=Floyd_adj_matrix(graph)
# for q in range(len(Graph)):
#     print(Path[q])
# print()
# for u in range(len(Graph)):
#      print(Graph[u])
# print('********************************')
#print(findPath(Path[3-1],3,5))
print()
print("Test Cases for Floyd's Algorithm using an Adjacency Matrix.")
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
Path, dist=Floyd_adj_matrix(test_case1)
start=1
end=8
print('Weight:',dist[start-1][end-1],end=' | Node Sequence: ')
findPath2(Path,start,end)
print('-----------------------------------------')
start=7
end=8
print('Weight:',dist[start-1][end-1],end=' | Node Sequence: ')
findPath2(Path,start,end)
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
Path, dist=Floyd_adj_matrix(test_case2)
# for i in range(len(Path)):
#     print(Path[i])
# print()
# for i in range(len(dist)):
#     print(dist[i])
start=2
end=8
print('Weight:',dist[start-1][end-1],end=' | Node Sequence: ')
findPath2(Path,start,end)
print('-----------------------------------------')
start=12
end=10
print('Weight:',dist[start-1][end-1],end=' | Node Sequence: ')
findPath2(Path,start,end)
print('-----------------------------------------')