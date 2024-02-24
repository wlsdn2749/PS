from collections import deque

###
N = int(input()) # 보드의 크기

K = int(input()) # 사과의 개수

apple_state = [[0] * (N+1) for _ in range(N+1)] # 사과가 있는 보드

for i in range(K):
    r, c = map(int, input().split())
    apple_state[r][c] = 1

L = int(input()) # 방향 변경 횟수

direction_queue = deque() # 방향 변경 queue

for i in range(L):
    x, c = input().split()
    direction_queue.append((int(x), c)) # (시간, 방향)
    
cur_snake_state = [[0] * (N+1) for _ in range(N+1)] # (1,1) 부터 시작
cur_snake_deque = deque()

cur_snake_state[1][1] = 1 # (1, 1) 시작
cur_snake_deque.appendleft((1, 1)) # 위치 저장

dx = [1, 0, -1, 0] # 동남서북
dy = [0, 1, 0, -1] # 처음 시작은 dx[0],dy[0]

cur_direction = 0 # 처음 시작은 동쪽

game = True # 게임 진행 여부

seconds = 0

while game: # loop 동안 1초씩 증가
    # [print(cur_snake_state[i]) for i in range(N+1)]
    # print(direction_queue)
    # print()
    seconds += 1
    
    cur_y, cur_x = cur_snake_deque[0] # 현재 위치
    
    cur_y += dy[cur_direction] # 다음 위치
    cur_x += dx[cur_direction] # 다음 위치로 이동
        
    # 이동했는데 벽이다?
    if cur_y == 0 or cur_y == N+1 or cur_x == 0 or cur_x == N+1:
        print(seconds) # 현재 초 출력
        game = False # 게임 set
        break
    
    # 이동했는데 자기자신의 몸과 부딫히면?
    elif cur_snake_state[cur_y][cur_x] == 1:
        print(seconds) # 현재 초 출력
        game = False # 게임 set
        break
    
    # 벽이나 자기자신의 몸과 부딫히지 않으면 아니면 뱀은 몸길이를 늘릴 수 있음
    else:
        # deque의 top [0] 은 항상 머리 bottom [-1]은 항상 꼬리
        cur_snake_deque.appendleft((cur_y, cur_x)) 
        cur_snake_state[cur_y][cur_x] = 1 
    
    # 이동했는데 사과다?
    if apple_state[cur_y][cur_x] == 1:
        apple_state[cur_y][cur_x] = 0 # 그 칸에 있는 사과 없어지고
        # 꼬리는 움직이지 않는다
    
    # 이동했는데 사과 아니다?
    elif apple_state[cur_y][cur_x] == 0:
        tail_y, tail_x = cur_snake_deque.pop() # 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다
        cur_snake_state[tail_y][tail_x] = 0
        
    # 이동을 마치고 ( X초가 끝난 뒤에 )
    if direction_queue and direction_queue[0][0] == seconds: # 방향을 바꿀때가 됬으면
        d_second, d_direction = direction_queue.popleft() 
        
        if d_direction == 'D': # 오른쪽
            cur_direction = (cur_direction+1)%4
        elif d_direction == 'L': # 왼쪽
            cur_direction = (cur_direction-1+4)%4
        
        
    
        
        
    
    
    


