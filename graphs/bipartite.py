def isBipartite(self, graph) -> bool:
        adj={}
        for i in range(len(graph)):
            adj[i]=graph[i]
        print(adj)
        v=[-1]*len(graph)
        
        def dfs(node,col,v):
            
            v[node]=col
            for nei in adj[node]:
                if v[nei]==-1:
                    if not dfs(nei, 1 - col, v):
                        return False
                else:
                    if v[nei]==v[node]:
                        return False
            return True
        for i in range(len(graph)):
            if v[i]==-1:
                if dfs(i,0,v)==False:
                    return False
        return True
