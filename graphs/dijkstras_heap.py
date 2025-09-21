import heapq
def dijkstra(self, V, edges, src):
    # code here
    adj={i:[] for i in range(V)}
    for u,v,w in edges:
        adj[u].append([v,w])
        adj[v].append([u,w])
    priority_queue = []
    dist=[float('inf')]*V
    dist[src]=0
    heapq.heappush(priority_queue,(0,src))
    while priority_queue:
        d,node=heapq.heappop(priority_queue)
        for nei,wei in adj[node]:
            if dist[node]+wei<dist[nei]:
                dist[nei]=d+wei
                heapq.heappush(priority_queue,(d+wei,nei))
    return dist


