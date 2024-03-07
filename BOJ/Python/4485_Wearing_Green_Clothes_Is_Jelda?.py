import heapq


def dijkstra(arr) -> list:    
    # start (0, 0)
    # end = (N-1, N-1)
    dy = [0, 1, 0, -1] # 동남서북
    dx = [1, 0, -1, 0]
    
    INF = 1_000_000
    distance_lst = [[INF]*N for _ in range(N)] # 거리 배열 초기화
    
    pq = []
    heapq.heappush(pq, (arr[0][0], (0, 0))) # value, node
    distance_lst[0][0] = arr[0][0]
    
    while pq:
        value, (y, x) = heapq.heappop(pq)
        
        for i in range(4):
            ddy = y + dy[i]
            ddx = x + dx[i]
            
            if 0 <= ddx < N and 0 <= ddy < N and distance_lst[ddy][ddx] > value+arr[ddy][ddx]: # In range and 거리 갱신을 한다면
            
                distance_lst[ddy][ddx] = min(distance_lst[ddy][ddx], value+arr[ddy][ddx]) # 거리 갱신
                heapq.heappush(pq, (distance_lst[ddy][ddx], (ddy, ddx)))
                
    return distance_lst
                
    
    
if __name__ == "__main__":
    
    cnt = 0
    while True:
        cnt += 1
        N = int(input())
        
        if N == 0:
            break
            
        arr = [list(map(int, input().split())) for _ in range(N)]
        
        distance_lst = dijkstra(arr)
        
        print(f"Problem {cnt}: {distance_lst[N-1][N-1]}")

    