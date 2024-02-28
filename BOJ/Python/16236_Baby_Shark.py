from collections import deque

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)] # board init


'''
    0 : 빈칸
    1,2,3,4,5,6 : 칸에 있는 물고기의 크기
    9 : 아기상어의 위치 
    
    아기상어는 크기 2부터 시작하며
    
    자기 크기보다 작은 물고기를 자기 크기만큼 먹어야 크기가 +1이 됨
    ex) 2보다 작은 물고기를 2개먹어야 3이됨
    
'''

def bfs(i, j, w):
    global movement
    
    visited = [[0] *len(board) for _ in range(len(board))] # visited init
    
    # dx = [0, -1, 0, 1] # 북서남동 순서
    # dy = [-1, 0, 1, 0] # 
    
    dx = [0, -1, 1, 0] # 
    dy = [-1, 0, 0, 1] # v2 = 북서동남
    
    
    dq = deque()
    dq.append((i, j, w, 0, 0)) # 상어 위치 pair, 상어 크기 w, 성장하기 위해 먹어야하는 물고기 개수 h, 경과한 시간 s
    visited[i][j] = 1 # 방문 여부
    

    possible_lst = []
    possible_sec = 1000 # init
    
    while dq: 
        y, x, shark_size, h, s = dq.popleft()
        
        # 이동했는데 먹을 수 있다면, 빈칸 아니라면? possible lst에 우선 넣기
        if board[y][x] < shark_size and board[y][x] != 0 and possible_sec >= s:
            possible_sec = s # 가능한 최소 시간
            possible_lst.append((y, x))
            
            
            # board[y][x] = 0 # 빈칸으로 만들고
            # h += 1
            
            # print("total_sec", total_sec+s, "sec", s, "shark_size", shark_size)
            # [print(board[i]) for i in range(len(board))]
            # print()
            # return (y,x,shark_size,h,s) # 현재 상어 위치, 상어 사이즈, 먹은 물고기 개수, 지난 초

        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            
            if 0 <= ddx < N and 0 <= ddy < N and not visited[ddy][ddx]: # 방문 여부와 경계선 체크
                # 만약 물고기 크기가 상어 크기보다 크다면 못지나감
                if board[ddy][ddx] > shark_size:
                    continue
                else:
                    dq.append((ddy, ddx, shark_size, h, s+1)) 
                    visited[ddy][ddx] = 1 # 방문
    
    if possible_lst:
        possible_lst.sort(key=lambda x:(x[0], x[1])) # 가장 위, 그다음 가장 왼쪽
        
        # print(possible_lst)
        y, x = possible_lst[0]
        board[y][x] = 0 # 빈칸으로 만들고
        h += 1
        
        # print("total_sec", total_sec+s, "sec", s, "shark_size", shark_size)
        # [print(board[i]) for i in range(len(board))]
        # print()
        return (y,x,shark_size,h,possible_sec) # 현재 상어 위치, 상어 사이즈, 먹은 물고기 개수, 지난 초
        
    else:
        movement = False
        return (0, 0, 0, 0, 0) # 더 이상 못먹음 엄마상어 요청
            
            
    
    
if __name__ == "__main__":
    cur_y, cur_x = 0, 0 # 현재 상어위치
    cur_shark_size = 2
    need_h = 0
    total_sec = 0
    movement = True
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                board[i][j] = 0
                cur_y, cur_x = i, j 
                break
            
    while movement:
        cur_y, cur_x, cur_shark_size, h, s = bfs(cur_y, cur_x, cur_shark_size)

        need_h += h
        total_sec += s
        
        if cur_shark_size == need_h: # 만약 사이즈만큼 먹었으면?
            cur_shark_size += 1
            need_h = 0 # 물고기 개수 0으로 초기화    
    
    print(total_sec)    
        
        
