import heapq
def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
    adj={i:[] for i in range(n)}
    for u,v,w in edges:
        adj[u].append([v,w])
        adj[v].append([u,w])
    def dij(src):
        dist=[float('inf')]*n
        dist[src]=0
        priority_queue=[]
        heapq.heappush(priority_queue,(0,src))
        while priority_queue:
            d,node=heapq.heappop(priority_queue)
            for nei,wei in adj[node]:
                if d+wei<dist[nei] and d+wei<=distanceThreshold:
                    dist[nei]=d+wei
                    heapq.heappush(priority_queue,(d+wei,nei))
        return dist
    min_neighbors = float('inf')
    best_city = -1

    for i in range(n):
        k=dij(i)
        num=n-k.count(float('inf'))-1
        if num < min_neighbors or (num == min_neighbors and i > best_city):
            min_neighbors = num
            best_city = i

    return best_city
