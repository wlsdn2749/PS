'''
    입력으로 양방향 간선의 최대치를 입력받는다.
    
    A -> B로 가는 DFS를 구하되 
    
    이분탐색으로 구하는 가중치가 지나갈 수 있으면 start를 올리고
    지나갈수 없다면 (모든 연결된 간선 탐색) -> end를 내린다
     
'''

import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y, cost): # cost는 최대 중량
    
    dq = deque()
    dq.append((x, y))
    while dq:
        
        x,y = dq.popleft()
        
        if x == y:
            return True
        
        for k,v in graphs[x].items():
            
            if not visited[k] and cost <= v: # 방문하지 않았고 현재 다리가 중량을 버틸 수 있는지
                visited[k] = 1
                dq.append((k, y))                
    
    return False # 도착못함
    
if __name__ == "__main__":
    N, M = map(int, input().split())
    
    graphs = [{} for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    
    min_weight, max_weight = sys.maxsize, 0
    for i in range(M):
        a,b,c = map(int, input().split())
        
        min_weight = min(c, min_weight)
        max_weight = max(c, max_weight)
        
        if graphs[a].get(b) == None: # 없다면
            graphs[a][b] = c
            graphs[b][a] = c
            
        elif graphs[a].get(b) < c: # 최대값 갱신
            graphs[a][b] = c
            graphs[b][a] = c # 양방향
            
    # print(graphs)
    x, y = map(int, input().split())
    start = min_weight
    end = max_weight
    middle = 0
    
    find_weight = 0
    while start <= end:
        
        middle = (start+end) // 2 
        # print(start, middle, end)
        
        visited = [0 for _ in range(N+1)]
        
        visited[x] = 1 # 시작점은 항상 방문 처리
        if bfs(x, y, middle) == True: # 현재 최대 중량으로 찾았다면
            start = middle+1
            find_weight = middle
        else: # 아직도 안된다면
            end = middle-1
            
    print(find_weight)
            