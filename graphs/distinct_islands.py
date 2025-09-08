def countDistinctIslands( grid ):
        m,n=len(grid),len(grid[0])
        v=[[0]*n for i in range(m)]
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or v[i][j]==1 or grid[i][j]!=1:
                return ""
            s=""
            v[i][j]=1
            s+=dfs(i+1,j)+'D'
            s+=dfs(i-1,j)+'U'
            s+=dfs(i,j+1)+'R'
            s+=dfs(i,j-1)+'L'
            return s
        seen=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and v[i][j]==0:
                    k=dfs(i,j)
                    seen.add(k)
        return len(seen)
                    