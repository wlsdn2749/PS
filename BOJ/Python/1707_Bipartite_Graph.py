import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def is_bipartite(v):
    
    for u in adj[v]:
        
        if visited[u] == False: # 아직 방문하지 않았다면
            
            visited[u] = True # 방문 처리 하고
            
            color[u] = not color[v] # 반대 컬러
            
            if not is_bipartite(u): # DFS
                return False
            
        elif color[u] == color[v]: # 같은 컬러라면?
            return False
        
    return True
        
K = int(input())

for test_case in range(K):
    
    V, E = map(int, input().split())
    
    adj = [[] for i in range(V+1)]
    visited = [0 for i in range(V+1)]
    color = [0 for i in range(V+1)]
    
    for i in range(E):
        a, b = map(int, input().split())
        
        adj[a].append(b)
        adj[b].append(a)
        
    
    visited[1] = True
    color[1] = 0
    
    for i in range(1, V+1):
        if not is_bipartite(i):
            print("NO")
            break
    else:
        print("YES")
        
    




