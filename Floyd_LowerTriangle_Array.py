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

def get_n_nodes(G):
    return 1+((int(math.sqrt(1+8*len(G)))-1)//2)

def get_weight(arr,i,j):
    weight=0
    if i!=j:
        if j<i:
            weight=arr[((i)*(i-1)//2)+j]
        else:
            weight=arr[((j)*(j-1)//2)+i]
    return weight

def Floyd_array(G):
    rowlength=get_n_nodes(G) 
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
                    newWeight=get_weight(G,i,k)+get_weight(G,k,j)
                    if newWeight<get_weight(G,i,j):
                        Path[i][j]=k
                        if i!=j:
                            if j<i:
                                G[((i)*(i-1)//2)+j]=newWeight
                            else:
                                G[((j)*(j-1)//2)+i]=newWeight
                    
    
    for r in range(rowlength-1):
        for s in range(r+1,rowlength):
            Path[s][r]=Path[r][s]
    return Path, G


graph=[ 5,
        7 ,inf,
        inf, 2 ,inf,
        inf,10 ,inf, 2]
#Path, dist=Floyd_array(graph)
#n=get_n_nodes(dist)
# for q in range(n):
#     print(Path[q])
# print()
# new=0
# for u in range(1,n):
#     print(dist[new:new+u])
#     new+=u
# print('-----------------------------------------')
# start=3
# end=5
# print(dist)
# print('Weight:',dist[((start)*(start-1)//2)+end],end=' | Node Sequence: ')
# print(start,end=',')
# findPath2(Path,start-1,end-1)
# print(end)
# print('-----------------------------------------')
print()
print("Test Cases for Floyd's Algorithm using a Lower Triangle Data Structure.")
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
Path, dist=Floyd_array(test_case1)
# n=get_n_nodes(dist)
start=1
end=8
# for q in range(n):
#     print(Path[q])
#print(((start)*(start-1)//2)+end,dist)
print('Weight:',get_weight(dist,start-1,end-1),end=' | Node Sequence: ')
# if end<start:
#     print('Weight:',dist[((start-1)*(start-2)//2)+end-1],end=' | Node Sequence: ')
# else:
#     print('Weight:',dist[((end-1)*(end-2)//2)+start-1],end=' | Node Sequence: ')
findPath2(Path,start,end)
print('-----------------------------------------')
start=7
end=8
print('Weight:',get_weight(dist,start-1,end-1),end=' | Node Sequence: ')
# if end<start:
#     print('Weight:',dist[((start-1)*(start-2)//2)+end-1],end=' | Node Sequence: ')
# else:
#     print('Weight:',dist[((end-1)*(end-2)//2)+start-1],end=' | Node Sequence: ')
findPath2(Path,start,end)
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
Path, dist=Floyd_array(test_case2)
# n=get_n_nodes(dist)
start=2
end=8
print('Weight:',get_weight(dist,start-1,end-1),end=' | Node Sequence: ')
# if end<start:
#     print('Weight:',dist[((start-1)*(start-2)//2)+end-1],end=' | Node Sequence: ')
# else:
#     print('Weight:',dist[((end-1)*(end-2)//2)+start-1],end=' | Node Sequence: ')
findPath2(Path,start,end)
print('-----------------------------------------')
start=12
end=10
print('Weight:',get_weight(dist,start-1,end-1),end=' | Node Sequence: ')
# if end<start:
#     print('Weight:',dist[((start-1)*(start-2)//2)+end-1],end=' | Node Sequence: ')
# else:
#     print('Weight:',dist[((end-1)*(end-2)//2)+start-1],end=' | Node Sequence: ')
findPath2(Path,start,end)
print('-----------------------------------------')