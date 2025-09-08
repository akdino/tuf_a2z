from collections import deque

def floodFill(image, sr: int, sc: int, color: int):
    initial_color = image[sr][sc]

    q=deque()
    q.append([sr,sc])
    m,n=len(image),len(image[0])
    v=[[0]*n for i in range(m)]
    drow=[+1,0,-1,0]
    dcol=[0,+1,0,-1]
    while q:
        
        r,c=q.popleft()
        image[r][c]=color
        for i in range(4):
            row=r+drow[i]
            col=c+dcol[i]
            if row>=0 and col>=0 and row<m and col<n and v[row][col]!=1 :
                if image[row][col]==initial_color:
                    q.append([row,col])
                    v[row][col]=1
                    image[row][col]=color
                    
    return image