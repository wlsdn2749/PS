import heapq

def search(y, x) -> str:
    cnt = 0
    for i in range(4):
        
        ddy = y + dy[i]
        ddx = x + dx[i]
        
        if 0 <= ddx < M and 0 <= ddy < N:
            if board[ddy][ddx] == 'g':
                cnt += 1
                
    return str(cnt)
                  
def dijkstra(y, x):
    
    pq = []
    
    INF = 1_000_000_000
    distance = [[(INF, INF)]*M for _ in range(N)]
    
    heapq.heappush(pq, (0, 0, y, x))
    
    # 인접한 쓰레기가 현재 최단거리보다 작을 경우 & 같은 경우 쓰레기 인접을 지나가는 횟수가 작은쪽으로 갱신
    def req(trash, trash_near, ddy, ddx):
        return not trash > distance[ddy][ddx][0] and trash_near < distance[ddy][ddx][1]
    
    while pq:
        trash, trash_near, y, x = heapq.heappop(pq)
        
        for i in range(4):
            ddy = y + dy[i]
            ddx = x + dx[i]
            
            if 0 <= ddy < N and 0 <= ddx < M and req(trash, trash_near, ddy, ddx):
                # 밟은 곳이 도착점
                if board[ddy][ddx] == 'F': 
                    distance[ddy][ddx] = (trash, trash_near)
                    
                # 밟은 곳이 trash    
                if board[ddy][ddx] == 'g': 
                    distance[ddy][ddx] = (trash+1, trash_near)
                    heapq.heappush(pq, (trash+1, trash_near, ddy, ddx))
                
                # 인접에 쓰레기가 있다면
                elif '1' <= board[ddy][ddx] <= '9':
                    distance[ddy][ddx] = (trash, trash_near+1)
                    heapq.heappush(pq, (trash, trash_near+1, ddy, ddx))
                        
                # 빈칸 인 경우
                elif board[ddy][ddx] == '0':
                    distance[ddy][ddx] = (trash, trash_near)
                    heapq.heappush(pq, (trash, trash_near, ddy, ddx))
                    
    return distance


if __name__ == "__main__":
    N, M = map(int, input().split())

    board = [list(map(str, input().strip())) for _ in range(N)]

    # print(board)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
                          
    start, end = (0, 0), (0, 0)
    for i in range(N):
        for j in range(M):
            if board[i][j] == '.':
                board[i][j] = search(i, j)
                
            if board[i][j] == 'S':
                start = (i, j)
                
            if board[i][j] == 'F':
                end = (i, j)
    
    
    distance = dijkstra(start[0], start[1])
    print(*distance[end[0]][end[1]])