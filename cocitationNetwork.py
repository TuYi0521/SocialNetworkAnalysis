import numpy as np
import networkx as nx
n = 3
# G=np.random.randint(0, 2, n**2).reshape(n, n)

G=nx.gnp_random_graph(n,0.5,directed=True)

DAG = nx.DiGraph([(u,v,{'weight':1}) for (u,v) in G.edges() if u<v])
temp = nx.is_directed_acyclic_graph(DAG)
print(temp)

# A = nx.adjacency_matrix(DAG)
E = DAG.edges()
# print(E)

A = np.zeros([n,n])


for (u,v) in G.edges():
    A[u][v] = 1
print(A)

for i in range(n):
    for j in range(n):
        if i == j:
            A[i][j] = 0
        if (i > j) and (A[i][j]==1) and (A[j][i]==1):
            temp = np.random.randint(0,2,1)
            if temp[0] == 0:
                A[j][i] = 0
            else:
                A[i][j] = 0
print("Citation Matrix")
print(A)

# np.savetxt('G_100.csv',A,fmt='%d',delimiter=',')

# cn = np.array(G) #citation network matrix in np form
# cocitation_network = np.zeros(cn.shape)
# for j in range(len(cn)):
#     if sum(cn[j])>=2:
#         list1 = []
#         for i in range(len(cn[j])):
#             if cn[j][i] ==1:
#                 list1.append(i)
#         for e in range(len(list1)):
#             for m in range(e+1, len(list1)):
#                     cocitation_network[list1[e]][list1[m]]+=1
#                     cocitation_network[list1[m]][list1[e]]+=1
# print()
# print("cocitation_network")
# print(cocitation_network)


# #Bibliographic coupling network
# bcn = np.zeros(cn.shape)
# for j in range(len(cn)):
#     list2 =[]
#     list3 =[]
#     for i in range(len(cn)):
#         list2.append(cn[i,j])
#         if cn[i,j]==1.:
#             list3.append(i)
#     if sum(list2)>=2:
#         for o in range(len(list3)):
#                 for m in range(o+1, len(list3)):
#                         bcn[list3[o]][list3[m]]+=1
#                         bcn[list3[m]][list3[o]]+=1
# print()
# print("Bibliographic coupling network")
# print(bcn)

