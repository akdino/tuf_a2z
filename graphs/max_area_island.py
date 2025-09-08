
def maxAreaOfIsland(self, grid):
    m,n=len(grid),len(grid[0])
    v=[[0]*n for i in range(m)]
    c=0
    def dfs(i,j):
        if i<0 or j<0 or i>=m or j>=n or v[i][j]==1 or grid[i][j]!=1:
            return 0
        
        v[i][j]=1
        area=1
        area+=dfs(i+1,j)
        area+=dfs(i-1,j)
        area+=dfs(i,j+1)
        area+=dfs(i,j-1)
        return area
    
    for i in range(m):
        for j in range(n):
            
            if grid[i][j]==1 and v[i][j]==0:
                c=max(c,dfs(i,j))



    return c