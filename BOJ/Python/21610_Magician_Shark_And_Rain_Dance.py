N, M = map(int, input().split())

arr = []

moves = []
pending_list = [[0]*N for _ in range(N)]

clouds_check = [[1]*N for _ in range(N)]

for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(M):
    d, s = map(int, input().split())
    moves.append((d, s))
    
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1] # 빈칸, 서, 북서, 북, 북동, 동, 동남, 남, 남서
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for move in moves:
    d, s = move
    
    bug_list = []
    clouds_check = [[1]*N for _ in range(N)]
    pending_list = [[0]*N for _ in range(N)]
    # 1. 모든 구름이 d 방향으로 s칸 이동한다.
    
    for cloud in clouds:
        y, x = cloud

        ddy = (y + dy[d] * s ) % N 
        if ddy < 0: # 음수 처리
            ddy += N
        ddx = (x + dx[d] * s ) % N 
        if ddx < 0: # 음수 처리
            ddx += N
        
        bug_list.append((ddy, ddx)) # 4에서 사용하기 위한 리스트
        clouds_check[ddy][ddx] = 0 # 구름 사라짐 처리
    # 2. 각 구름에서 비가 내려 구름이 잇는 칸의 바구니에 저장된 물의 양이 1 증가 한다.
        
        arr[ddy][ddx] += 1
    
    # 3. 구름이 모두 사라진다.
    # [ print(arr[i]) for i in range(N)] 
    # print(clouds)
    # print()
    # print(bug_list)
    
    # for cloud in clouds:
    #     y, x = cloud
    #     clouds_check[y][x] = 0 # 구름 사라짐 처리
        
    clouds = []
        
    
    # 4. 2에서 물이 증가한 칸 (r,c)에 물복사 버그 마법 시전
    
    for cloud in bug_list:
        y, x = cloud
        
        # 대각선 방향으로 거리가 1인 칸에 있는 물이 있는 바구니 수만큼 
        # (r,c)에 있는 바구니의 물이 증가
        for i in [2,4,6,8]:
            ddy = y + dy[i]
            ddx = x + dx[i]
            
            if 0 <= ddy < N and 0 <= ddx < N: # 이때 경계 안쪽만 체크
                if arr[ddy][ddx] >= 1: # 물이 있다면
                    pending_list[y][x] += 1 # 바구니 개수만큼 증가
                    

    
    # 4. 에서 실제로 증가하는 부분
    # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생김
    # 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니여야함
    
    for i in range(N): 
        for j in range(N): 
            arr[i][j] += pending_list[i][j]
            
            # 3에서 구름이 사라진 칸이 아니면서
            # 바구니에 저장된 물의 양이 2이상인 모든 칸에 구름이 생김
            if clouds_check[i][j] == 1 and arr[i][j] >= 2: 
                arr[i][j] -= 2 # 물의 양 2 감소
                clouds.append((i, j))
                
                
    # print("구름이 생긴후")
    
    # [ print(arr[i]) for i in range(N)] 
    # print()
    
print(sum(map(sum, arr)))
                
                
                
        
        
        
        
    
    





    
    