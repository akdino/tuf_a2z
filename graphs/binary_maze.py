from collections import deque
def shortestPathBinaryMatrix( grid) -> int:
    if grid[0][0]==1 or grid[len(grid)-1][len(grid)-1]==1:
        return -1
    if grid==[[0]]:return 1

    n=len(grid)
    dist=[[float('inf')]*n for i in range(n)]
    dist[0][0]=0
    q=deque()
    q.append((1,0,0))
    drow=[-1,-1,-1,0,0,1,1,1]
    dcol=[-1,0,1,+1,-1,-1,0,+1]
    while q:
        d,i,j=q.popleft()
        for m in range(8):
            r=i+drow[m]
            c=j+dcol[m]
            if 0<=r<n and 0<=c<n and grid[r][c]==0:
                if dist[r][c] == float('inf'):
                    dist[r][c] = dist[i][j] + 1
                    q.append((d+1,r, c))
                    if r==n-1 and c==n-1:
                        return d+1
    return -1