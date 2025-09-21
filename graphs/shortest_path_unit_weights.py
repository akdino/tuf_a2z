from collections import deque
def shortestPath(self, ad, src):
        # code here
        d=[float('inf')]*len(ad)
        d[src]=0
        adj={i:ad[i] for i in range(len(ad))}
        
        q=deque()
        q.append([src,0])
        while q:
            node,dist=q.popleft()
            for nei in adj[node]:
                if d[nei]>dist+1:
                    d[nei]=dist+1
                    q.append([nei,dist+1])
        for i in range(len(d)):
            if d[i] == float('inf'):d[i] = -1
        return d