from collections import deque
def topoSort( V, edges):
        # Code here
        adj={i: [] for i in range(V)}
        for u, x in edges:
            adj[u].append(x)
        q=deque()
        v=[]
        indegree=[0]*V
        for u,x in edges:
            indegree[x]+=1
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        top=[]
        while q:
            node=q.popleft()
            top.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
                
            
        return top