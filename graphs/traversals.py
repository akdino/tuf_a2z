from collections import deque

def bfs():
    v=set()
    source=int(input(f'enter first node'))
    v.add(source)
    q=deque()
    q.append(source)
    adj={0: [1, 2], 1: [0, 2], 2: [1, 3, 0, 4], 3: [2], 4: [2]}
    while q:
        node=q.popleft()
        print(node)
        for nei in adj[node]:
            if nei not in v:
                v.add(nei)
                q.append(nei)
def dfs():
    n=5
    adj={0: [1, 2], 1: [0, 2], 2: [1, 3, 0, 4], 3: [2], 4: [2]}
    visited=[0]*n
    source=int(input(f'enter first node'))
    lst=[]
    
    
    def rec(node):
        visited[node]=1
        print(node)
        for nei in adj[node]:
            if not visited[nei]:
                rec(nei)
    rec(source)
    print("=======")
    def itr():
        seen=set()
        seen.add(source)
        stack=[source]
        while stack:
            node=stack.pop()
            print(node)
            for nei in adj[node]:
                if nei not in seen:
                    seen.add(nei)
                    stack.append(nei)
    itr()
dfs()