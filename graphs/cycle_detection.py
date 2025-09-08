from collections import deque
#bfs
V=3
edges=[]#pair of edges
adj={}
for i in range(V):
    adj[i]=[]
for i in edges:
    adj[i[0]].append(i[1])
    adj[i[1]].append(i[0])
q=deque()
v=[0]*V
def bfs():
    for src in range(V):
        if not v[src]:
            q.append([src,-1])
            v[src]=1
            while q:
                node, parent=q.popleft()
                for nei in adj[node]:
                    if not v[nei]:
                        v[nei]=1
                        q.append([nei,node])
                
                    elif parent!=nei:
                        return True
    return False
def dfs(node,parent):
    v[node]=1
    for nei in adj[node]:
        if not v[nei]:
            if dfs(nei,node):return True
        elif nei!=parent:
            return True
    return False
for i in range(V):
    if not v[i]:
        if dfs(i,-1):print("yes")
print("false")

