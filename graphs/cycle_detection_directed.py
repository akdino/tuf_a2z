def isCycle(self, V, edges):
    # code here
    v=[0]*V
    pv=[0]*V
    
    adj={i: [] for i in range(V)}
    for u, x in edges:
        adj[u].append(x)
    def dfs(node,pv,v):
        pv[node]=1  
        v[node]=1
        for nei in adj[node]:
            if not v[nei]:
                if dfs(nei,pv,v)==True:
                    return True
            elif pv[nei]:return True
        pv[node]=0
        return False
    for i in range(V):
        if not v[i]:
            if dfs(i,pv,v)==True:
                return True
    return False
