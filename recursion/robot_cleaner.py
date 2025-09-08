def rec(matrix):
    def rec(i,j,v,matrix):
        if i<=0 or j<=0 or i>m or j>n:
            return
        if v[i][j]:
            return
        if matrix[i][j]=="#":
            return
        v[i][j]=1
        rec(i+1,j,v,matrix)
        rec(i-1,j,v,matrix)
        rec(i,j-1,v,matrix)
        rec(i,j+1,v,matrix)
matrix=[]
c=0
m,n=len(matrix),len(matrix[0])
v=[[0]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        if matrix[i][j]=="*":
            c+=1
            rec(i,j,v,matrix)
print(c)