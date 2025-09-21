import heapq
def minimumEffortPath(self, heights) -> int:
        m,n=len(heights),len(heights[0])
        dist=[[float('inf')]*n for i in range(m)]
        
        dist[0][0]=0
        pq = [(0, 0, 0)] 
        drow=[0,1,0,-1]
        dcol=[1,0,-1,0]
        while pq:
            d,i,j=heapq.heappop(pq)
            if i==m-1 and j==n-1:
                return d
            for dr in range(4):
                nr = i + drow[dr]
                nc = j + dcol[dr]
                if 0<=nr<m and 0<=nc<n:
                    new=max(d,abs(heights[i][j]-heights[nr][nc]))
                    if new<dist[nr][nc]:
                        dist[nr][nc]=new
                        heapq.heappush(pq,(new,nr,nc))
        return 0