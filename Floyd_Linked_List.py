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

def findWeight(G,start,end):
    node=G[start-1].head.next
    while(node!=G[start-1].tail):
        if node.val[0]==end-1:
            weight=node.val[1]
            break
        node=node.next
    if start==end:
        weight=0
    return weight

def Floyd_Linked_List(G):
    rowlength=len(G)
    Path=[]
    W=[]
    #Make Path
    for x in range(rowlength):
        node=G[x].head.next
        Path.append([])
        for y in range(rowlength):
            Path[x].append(-1)
            if node.val!=None:
                if y==node.val[0]:
                    node=node.next
                    

    for k in range(rowlength):
        for i in range(rowlength):
            #first: start G[i]
            first=G[i].head.next
            while (first!=G[i].tail):
                if first.val[0]==k:
                    first_half=first.val[1]
                    break
                first=first.next
            if i==k:
                first_half=0
            elif first==G[i].tail:
                first_half=inf
            #second: start G[k].head.next if not this one then second_half=inf
            second=G[k].head.next
            #oldNode: start G[i][j]
            oldNode=G[i].head.next

            for j in range(rowlength):
                #oldNode: if G[i][j] isn't this one then oldWeight=inf
                flag=0
                if (oldNode!=G[i].tail):
                    if oldNode.val[0]==j:
                        oldWeight=oldNode.val[1]
                        flag=1
                    elif i==j:
                        oldWeight=0
                    else:
                        oldWeight=inf
                elif i==j:
                    oldWeight=0
                else:
                    oldWeight=inf
                    
                #oldNode: else if G[i].val[0]==j then oldWweight=G[i].val[1] 
                    #oldeNode.next: go to next node in G[i]
                #first: refind G[k][j] every time
                    #Or this, but needs work before this improvement if G[k][j] isn't this one (val[0]!=j) then second_half=inf
                if (second!=G[k].tail):
                    if second.val[0]==j:
                        second_half=second.val[1]
                        second=second.next
                    elif k==j:
                        second_half=0
                    else:
                        second_half=inf
                elif k==j:
                    second_half=0
                else:
                    second_half=inf
                
                newWeight=first_half+second_half
                if newWeight<oldWeight: 
                    Path[i][j]=k
                    #oldW: if the weight isn't there then add it to the linked list before this node (should be in order)
                    if oldWeight==inf and newWeight!=inf:
                        newNode=Node(val=[j,newWeight])
                        G[i].add(newNode,oldNode.prev)
                    else:
                        oldNode.val[1]=newWeight

                if flag==1:
                    oldNode=oldNode.next


    return Path, G

graph=[ [ 0 , 5 , 7 ,inf,inf],
        [ 5 , 0 ,inf, 2 ,10 ],
        [ 7 ,inf, 0 ,inf,inf],
        [inf, 2 ,inf, 0 , 2 ],
        [inf,10 ,inf, 2 , 0 ]]
# graph=[ [0, 4, inf],
#        [4, 0, 3],
#        [inf, 3, 0]]
# graph=graph_translate_to_LL(graph)
#print("-------------------_Test Zone_---------------------")
# Path, G=Floyd_Linked_List(graph)
# print("---------------------------------------------------")
# for i in range(len(Path)):
#     print(Path[i])
# print()
# for q in range(len(G)):
#     node=G[q].head.next
#     while node!=G[q].tail:
#         print(node.val, end=', ')
#         node=node.next
#     print()
# print()
# start=1
# end=3
# start=3
# end=5
# node=G[start-1].head.next
# while(node!=G[start-1].tail):
#     if node.val[0]==end-1:
#         weight=node.val[1]
#         break
#     node=node.next
# if start==end:
#     weight=0
# print('Weight:',weight,end=' | Node Sequence: ')
# print(start,end=',')
# findPath2(Path,start-1,end-1)
# print(end)

print()
print("Test Cases for Floyd's Algorithm using an Array of Linked Lists.")
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
Path, G=Floyd_Linked_List(graph)
weight=findWeight(G,start,end)
print('Weight:',weight,end=' | Node Sequence: ')
#print(start,end=',')
findPath2(Path,start,end)
#print(end)
print('-----------------------------------------')
start=7
end=8
weight=findWeight(G,start,end)
print('Weight:',weight,end=' | Node Sequence: ')
#print(start,end=',')
findPath2(Path,start,end)
#print(end)
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
Path, G=Floyd_Linked_List(graph)
weight=findWeight(G,start,end)
print('Weight:',weight,end=' | Node Sequence: ')
findPath2(Path,start,end)
print('-----------------------------------------')
start=12
end=10
weight=findWeight(G,start,end)
print('Weight:',weight,end=' | Node Sequence: ')
findPath2(Path,start,end)
print('-----------------------------------------')