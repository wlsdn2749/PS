
# 0 : 동쪽
# 1 : 남쪽
# 2 : 서쪽
# 3 : 북
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1] # 동남서북

def bfs(i, j):

    if i == 0 or j == 0 or i == N-1 or j == N-1: # 전원선에서 한 칸 떨어져있는 경우 고려 안함
        return None
    
    lines = []
    
    for idx in range(4):
        cnt = 0
        while True:
            cnt += 1
            ddx = j + dx[idx] * cnt
            ddy = i + dy[idx] * cnt
            
            # Out of Range인 경우 즉, Power에 연결되는 경우 전선이 연결될 수 있는 방향을 lines에 넣어줌
            if not ( 0 <= ddx < N and 0 <= ddy < N ):
                lines.append(idx)
                break
                
            # 이동했는데 이미 core가 있는경우
            # 이 방향은 core가 있어서 연결 불가
            if board[ddy][ddx] == 1:
                break
    
    if not lines:
        return None
    
    # 이 시점에서 lines에는 (i, j)에 있는 코어가 어디로 직선을 그을 수 있는지를 담고 있음
    # print(i, j, lines)
    return (i, j, lines) # i,j와 어디로 직선을 그을 수 있는지 lines를 튜플로 리턴

def bt(idx, k):
    
    global min_len, max_k
    
    if len(cores) == 0:
        min_len = 0
        return
    
    
    if idx >= len(cores): # 더이상 할 곳 없다
        
        if max_k > k-1:
            return
        
        cur_len = 0
        for i in range(N):
            for j in range(N):
                if board[i][j] == 2: # 선분
                    cur_len += 1
                    
        if max_k == k-1:
            min_len = min(cur_len, min_len) 
            max_k = k-1
            
        elif max_k < k-1:
            min_len = cur_len
            max_k = k-1
            
        # print("max_k =:", max_k, "k", k-1, "cur_len", cur_len)    
        # [print(board[i]) for i in range(len(board))]
        return 
    
    y, x, lines = cores[idx] # idx번째 cores 정보
    
    for direction in lines: # 모든 라인s에 대해
        traces = []
        branch = False
        cnt = 0
        while True:
            cnt += 1
            ddy = y + dy[direction] * cnt
            ddx = x + dx[direction] * cnt
            
            # 전원부라면 종료
            if not ( 0 <= ddx < N and 0 <= ddy < N ):
                branch = True
                break
            
            if board[ddy][ddx] == 0:
                board[ddy][ddx] = 2 # 선분 긋고
                traces.append((ddy, ddx))
                continue
            
            if board[ddy][ddx] == 2: # 이미 있던 선분에 라인을 긋게되면
                for ty, tx in traces: # rollback
                    board[ty][tx] = 0
                # branch = False # 가지치기
                # k = k-1
                traces = []
                break
            
        if branch:
            bt(idx+1, k+1)
        else:
            bt(idx+1, k)
        
        for ty, tx in traces: # rollback
            board[ty][tx] = 0
            
    bt(idx+1, k) # 아무대도 못가는경우
            
        
if __name__ == "__main__":
    T = int(input())
    
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):

        N = int(input()) # 7 <= N <= 12

        board = [list(map(int, input().split())) for _ in range(N)] # init
        cores = [] # 코어 기록
        
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    result = bfs(i, j)
                    
                    if result == None: # 어디로도 갈 수 없거나, 혹은 가장자리에 있거나
                        continue
                    else:
                        cores.append(result)


        # cores에는 (y,x, lines: list)가 들어가 있음
        min_len = 1_000_000
        max_k = 0
        for i in range(len(cores)):
            bt(i, 1)
            
        if min_len == 1_000_000:
            min_len = 0
            
        print(f"#{test_case} {min_len}")

    

        

