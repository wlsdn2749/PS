from collections import deque, defaultdict

max_distance = 0
dd = defaultdict(int)

def bfs(graph, visited):
    global max_distance, dd
    dq = deque()
    dq.append((1, 0)) # 현재 노드, 이동한 거리
    visited[1] = 1 # 현재 노드 방문처리
    
    while dq:
        cur_node, dist = dq.popleft()
        
        if dist > max_distance: # 최장거리 갱신
            max_distance = dist
        
        if max_distance == dist:
            dd[dist] += 1
            
            
        for node in graph[cur_node]:
            if visited[node] == 0:
                visited[node] = 1
                dq.append((node, dist+1))
    
def solution(n, edge):
    
    visited = [0 for _ in range(n+1)]

    graph = [[] for _ in range(n+1)]
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    bfs(graph, visited)
    
    answer = dd[max_distance]
    return answer