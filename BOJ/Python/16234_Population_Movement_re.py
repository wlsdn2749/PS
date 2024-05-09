from collections import deque

def union_process(union_lst):
    union_population = sum(map(lambda x,y: A[x][y], *zip(*union_lst)))
    union_count = len(union_lst)
    union_mean = union_population // union_count 
    # print(union_lst, union_count)
    
    for y, x in union_lst:
        A[y][x] = union_mean # 소수점 버림
    
def bfs(i, j, visited):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    
    dq = deque()
    union_lst = list()
    
    dq.append((i, j))
    visited[i][j] = True
    union_lst.append((i, j))
    
    while dq:
        y, x = dq.popleft()
        
        for r in range(4):
            ddy = y + dy[r]
            ddx = x + dx[r]
            
            if 0 <= ddy < N and 0 <= ddx < N:
                if not visited[ddy][ddx] and L <= abs(A[ddy][ddx] - A[y][x]) <= R:
                    union_lst.append((ddy, ddx))
                    visited[ddy][ddx] = True
                    dq.append((ddy,ddx))
                    
    
    if len(union_lst) >= 2:
        union_process(union_lst)
        return True
    
    return False
    
    
if __name__ == "__main__":
    N, L, R = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    
    days = 0
    while True:
        is_moved = False
        visited = [[False] * N for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                if not visited[i][j]: 
                    if bfs(i, j, visited):
                        is_moved = True
        
        
        # [print(A[i]) for i in range(N)]
        # print(" ")
        if is_moved:
            days += 1
        
        else:
            print(days)
            break
            
                    
            
            