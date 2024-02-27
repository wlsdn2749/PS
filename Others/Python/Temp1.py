import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    
numbers = [0 for _ in range(0, 11)] # 1~10

visited = [[0] * N for _ in range(N)]


def bfs(i, j, num):
    dq = deque()
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    dq.append((i, j))
    visited[i][j] = 1
    
    result = 1
    
    while dq:
        y, x = dq.pop() # 
        
        for k in range(4):
            ddx = x + dx[k]
            ddy = y + dy[k]
            
            if 0 <= ddx < N and 0 <= ddy < N: # 범위
                if arr[ddy][ddx] == num and not visited[ddy][ddx]: # 같은 집합이고, 방문하지 않았다면
                    dq.append((ddy, ddx))
                    visited[ddy][ddx] = 1
                    result+=1
                    
    return result

    
for num in range(1, 11):
    # init
    
    visited = [[0] * N for _ in range(N)]
    # bfs
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and arr[i][j] == num:
                numbers[num] = max(bfs(i, j, num), numbers[num])
                
print(*numbers[1:])
    
    
    
    