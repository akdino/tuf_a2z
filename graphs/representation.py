#adjacency matrix
n=5
edge=int(input(f'enter number of edges'))
edges=[]
matrix=[[0]*n for i in range(n)]
for i in range(n):
    matrix[i][i]=1
for i in range(edge):
    u=int(input(f'edge from node:'))
    v=int(input(f'edge to node:'))
    edges.append([u,v])

print(matrix,edges)


#adjacency list
adjacency_list={}
for i in range(n):
    adjacency_list[i]=[]
for i in edges:
    adjacency_list[i[0]].append(i[1])
    adjacency_list[i[1]].append(i[0])
print(adjacency_list)
