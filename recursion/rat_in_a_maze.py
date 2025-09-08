'''
1 0 0 0
1 1 0 0
1 1 0 0
0 1 1 1

'''
n=4
v = [[0 for _ in range(n)] for _ in range(n)]
mat=[[1,0,0,0],[1,1,0,0],[1,1,0,0],[0,1,1,1]]
def rec(i,j,final,mat,v,n,path):
    if i==n-1 and j==n-1:
        print(path[:])
        return 


    #downwards
    if (i+1<n and mat[i+1][j]==1 and v[i+1][j]==0  ):
        v[i+1][j]=1
        rec(i+1,j,final,mat,v,n,path+['D'])
        v[i+1][j]=0
    
    #left
    if ( j-1>=0 and mat[i][j-1]==1 and v[i][j-1]==0 ):
        v[i][j-1]=1
        rec(i,j-1,final,mat,v,n,path+['L'])
        v[i][j-1]=0
    
    #right
    if ( j+1<n and mat[i][j+1]==1 and v[i][j+1]==0 ):
        v[i][j+1]=1
        rec(i,j+1,final,mat,v,n,path+['R'])
        v[i][j+1]=0
    
    #upwards
    if (i-1>=0 and mat[i-1][j]==1 and v[i-1][j]==0  ):
        v[i-1][j]=1
        rec(i-1,j,final,mat,v,n,path+['U'])
        v[i-1][j]=0



final = []
rec(0, 0, final, mat, v, n, [])
print(final)
