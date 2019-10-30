from Dijkstra_Adjacency_Matrix import *
from Dijkstra_LowerTriangle_Array import *
from Dijkstra_Linked_List import *
from Floyd_Adjacency_Matrix import *
from Floyd_LowerTriangle_Array import *
from Floyd_Linked_List import *
from Graph_Generation import Generate_Complete_Graph,Generate_Sparse_Graph,graph_translate_to_LL,graph_translate_to_LowTri
from time import perf_counter
import matplotlib.pyplot as plt

#Dijkstra's:
#Adjacency Matrix
#Lower Triangle
#Linked List

#FLoyd's:
#Adjacency Matrix
#Lower Triangle
#Linked List


#list of test cases added 400,600
Test_Cases=[5,10,50,100,200,400,500,600]#,1000]
#runs=10
RT_Complete_Dijkstra_Adjacency_Matrix=[]
RT_Complete_Dijkstra_Lower_Triangle=[]
RT_Complete_Dijkstra_Linked_List=[]
RT_Complete_Floyd_Adjacency_Matrix=[]
RT_Complete_Floyd_Lower_Triangle=[]
RT_Complete_Floyd_Linked_List=[]

RT_Sparse_Dijkstra_Adjacency_Matrix=[]
RT_Sparse_Dijkstra_Lower_Triangle=[]
RT_Sparse_Dijkstra_Linked_List=[]
RT_Sparse_Floyd_Adjacency_Matrix=[]
RT_Sparse_Floyd_Lower_Triangle=[]
RT_Sparse_Floyd_Linked_List=[]
#make all the lists above already have size = runs
#run 10 times and average 
#for r in range(runs):
for i in range (len(Test_Cases)):
    print(i)
    n=Test_Cases[i]
    #Initial for Dijkstra's
    initial=1
#COMPLETE
    #Generate Complete Graphs:
    #Adjacency Matrix
    Complete_Adjacency_Matrix = Generate_Complete_Graph(n)
    # for j in range(len(Adjacency_Matrix)):
        # print(Adjacency_Matrix[j])

    #Lower Triangle
    Complete_Lower_Triangle = graph_translate_to_LowTri(Complete_Adjacency_Matrix)
    # print (Lower_Triangle)

    #Linked List
    Complete_Linked_List_Array = graph_translate_to_LL(Complete_Adjacency_Matrix)
    # for k in range(len(Linked_List_Array)):
    #     node=Linked_List_Array[k].head.next
    #     while node!=Linked_List_Array[k].tail:
    #         print(node.val)
    #         node=node.next
    
    #Test
    #Dijkstra's: Adjacency Matrix add runtime to list
    Ti=perf_counter()
    Dijkstra_adj_matrix(Complete_Adjacency_Matrix,initial)
    Tf=perf_counter()
    RT_Complete_Dijkstra_Adjacency_Matrix.append(Tf-Ti)
    #Dijkstra's: Lower Triangle add runtime to list
    Ti=perf_counter()
    Dijkstra_array(Complete_Lower_Triangle,initial)
    Tf=perf_counter()
    RT_Complete_Dijkstra_Lower_Triangle.append(Tf-Ti)
    #Dijkstra's: Linked List add runtime to list
    Ti=perf_counter()
    Dijkstra_LL(Complete_Linked_List_Array,initial)
    Tf=perf_counter()
    RT_Complete_Dijkstra_Linked_List.append(Tf-Ti)

    #Test
    #FLoyd's: Adjacency Matrix
    #add runtime to list
    Ti=perf_counter()
    Floyd_adj_matrix(Complete_Adjacency_Matrix)
    Tf=perf_counter()
    RT_Complete_Floyd_Adjacency_Matrix.append(Tf-Ti)


    #FLoyd's: Lower Triangle
    #add runtime to list
    Ti=perf_counter()
    Floyd_array(Complete_Lower_Triangle)
    Tf=perf_counter()
    RT_Complete_Floyd_Lower_Triangle.append(Tf-Ti)

    #FLoyd's: Linked List
    #add runtime to list
    Ti=perf_counter()
    Floyd_Linked_List(Complete_Linked_List_Array)
    Tf=perf_counter()
    RT_Complete_Floyd_Linked_List.append(Tf-Ti)

#SPARSE:
    #Generate Sparse Graphs:
    #Adjacency Matrix
    Sparse_Adjacency_Matrix = Generate_Sparse_Graph(n)
    #Lower Triangle
    Sparse_Lower_Triangle = graph_translate_to_LowTri(Sparse_Adjacency_Matrix)
    #Linked List
    Sparse_Linked_List_Array = graph_translate_to_LL(Sparse_Adjacency_Matrix)
    
    #Test
    #Dijkstra's: Adjacency Matrix
    #add runtime to list
    Ti=perf_counter()
    Dijkstra_adj_matrix(Sparse_Adjacency_Matrix,initial)
    Tf=perf_counter()
    RT_Sparse_Dijkstra_Adjacency_Matrix.append(Tf-Ti)

    #Dijkstra's: Lower Triangle
    #add runtime to list
    Ti=perf_counter()
    Dijkstra_array(Sparse_Lower_Triangle,initial)
    Tf=perf_counter()
    RT_Sparse_Dijkstra_Lower_Triangle.append(Tf-Ti)

    #Dijkstra's: Linked List
    #add runtime to list
    Ti=perf_counter()
    Dijkstra_LL(Sparse_Linked_List_Array,initial)
    Tf=perf_counter()
    RT_Sparse_Dijkstra_Linked_List.append(Tf-Ti)
    
    #Test
    #FLoyd's: Adjacency Matrix
    #add runtime to list
    Ti=perf_counter()
    Floyd_adj_matrix(Sparse_Adjacency_Matrix)
    Tf=perf_counter()
    RT_Sparse_Floyd_Adjacency_Matrix.append(Tf-Ti)
    
    #FLoyd's: Lower Triangle
    #add runtime to list
    Ti=perf_counter()
    Floyd_array(Sparse_Lower_Triangle)
    Tf=perf_counter()
    RT_Sparse_Floyd_Lower_Triangle.append(Tf-Ti)
    
    #FLoyd's: Linked List
    #add runtime to list
    Ti=perf_counter()
    Floyd_Linked_List(Sparse_Linked_List_Array)
    Tf=perf_counter()
    RT_Sparse_Floyd_Linked_List.append(Tf-Ti)

#output runtimes to a file
#plot run times
print(RT_Complete_Dijkstra_Adjacency_Matrix)
print(RT_Complete_Dijkstra_Lower_Triangle)
print(RT_Complete_Dijkstra_Linked_List)
print(RT_Complete_Floyd_Adjacency_Matrix)
print(RT_Complete_Floyd_Lower_Triangle)
print(RT_Complete_Floyd_Linked_List)

print(RT_Sparse_Dijkstra_Adjacency_Matrix)
print(RT_Sparse_Dijkstra_Lower_Triangle)
print(RT_Sparse_Dijkstra_Linked_List)
print(RT_Sparse_Floyd_Adjacency_Matrix)
print(RT_Sparse_Floyd_Lower_Triangle)
print(RT_Sparse_Floyd_Linked_List)  

plt.plot(Test_Cases,RT_Complete_Dijkstra_Adjacency_Matrix, label='Adjacency Matrix')
plt.plot(Test_Cases,RT_Complete_Dijkstra_Lower_Triangle, label='Lower Triangle Array')
plt.plot(Test_Cases,RT_Complete_Dijkstra_Linked_List, label='Linked Lists')
plt.legend()
plt.title("Run Time: Dijkstra's Algorithm, Complete Graph")
plt.xlabel("Graph Size (number of vertices)")
plt.ylabel("Run Time (seconds)")
plt.show()

plt.plot(Test_Cases,RT_Complete_Floyd_Adjacency_Matrix, label='Adjacency Matrix')
plt.plot(Test_Cases,RT_Complete_Floyd_Lower_Triangle, label='Lower Triangle Array')
plt.plot(Test_Cases,RT_Complete_Floyd_Linked_List, label='Linked Lists')
plt.legend()
plt.title("Run Time: Floyd's Algorithm, Complete Graph")
plt.xlabel("Graph Size (number of vertices)")
plt.ylabel("Run Time (seconds)")
plt.show()

plt.plot(Test_Cases,RT_Sparse_Dijkstra_Adjacency_Matrix, label='Adjacency Matrix')
plt.plot(Test_Cases,RT_Sparse_Dijkstra_Lower_Triangle, label='Lower Triangle Array')
plt.plot(Test_Cases,RT_Sparse_Dijkstra_Linked_List, label='Linked Lists')
plt.legend()
plt.title("Run Time: Dijkstra's Algorithm, Sparse Graph")
plt.xlabel("Graph Size (number of vertices)")
plt.ylabel("Run Time (seconds)")
plt.show()

plt.plot(Test_Cases,RT_Sparse_Floyd_Adjacency_Matrix, label='Adjacency Matrix')
plt.plot(Test_Cases,RT_Sparse_Floyd_Lower_Triangle, label='Lower Triangle Array')
plt.plot(Test_Cases,RT_Sparse_Floyd_Linked_List, label='Linked Lists')
plt.legend()
plt.title("Run Time: Floyd's Algorithm, Sparse Graph")
plt.xlabel("Graph Size (number of vertices)")
plt.ylabel("Run Time (seconds)")
plt.show()