def dijkstra(self, V, edges, src):
        # code here
        adj={i:[] for i in range(V)}
        for u,v,w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w])
        s=set()
        dist=[float('inf')]*V
        dist[src]=0
        s.add((0,src))
        while s:
            d,u=min(s)
            s.remove((d,u))
            for v,w in adj[u]:
                if d+w<dist[v]:
                    if dist[v] != float('inf'):
                        s.discard((dist[v],v))
                    dist[v]=dist[u]+w
                    s.add((dist[v], v))
        return dist