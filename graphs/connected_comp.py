'''
connected comp template:
visted=[0]*(number of nodes)
for i in range(number of nodes):   
    if not visited[i]:
        traversal(i)
traversal: for every node it visits, visited[i]=1

'''
def findCircleNum(self, isConnected: List[List[int]]) -> int:
    n=len(isConnected)
    visit=[0]*n

    def dfs(i,lst):
        visit[i]=1
        nei_nodes=[i for i in range(n) if lst[i]==1]
        for nei in nei_nodes:
            if not visit[nei] and i!=nei:
                dfs(nei,isConnected[nei])
    c=0
    for i in range(n):
        if not visit[i]:
            c+=1
            dfs(i,isConnected[i])
    return c




