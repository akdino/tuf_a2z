def topoSort( V, edges):
        # Code here
        v=[0]*V
        adj={i:[] for i in range(V)}
        for u,x in edges:
            adj[u].append(x)
        stack=[]
        def dfs(node):
            v[node]=1
            
            for nei in adj[node]:
                if not v[nei]:
                    dfs(nei)
            stack.append(node)
        
        for i in range(V):
            if not v[i]:
                dfs(i)
        k=[]
        while stack:
            k.append(stack.pop())
        return k