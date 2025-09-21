def shortestPath(V: int, E: int,edges):
        adj={i:[] for i in range(V)}
        for u,v,w in edges:
            adj[u].append([v,w])
        vis=[0]*V
        stack=[]
        def dfs(node):
            vis[node]=1
            for nei,wei in adj[node]:
                if not vis[nei]:
                    dfs(nei)
                    
            stack.append(node)
                
        for i in range(V):
            if not vis[i]:
                dfs(i)
        dist=[float('inf')]*V
        dist[0]=0
        while stack:
            node=stack.pop()
            for nei,wei in adj[node]:
                if dist[node]+wei<dist[nei]:
                    dist[nei]=dist[node]+wei
        for i in range(len(dist)):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist