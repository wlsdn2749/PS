from itertools import combinations
from collections import deque
from copy import deepcopy

N, M, D = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
# board의 N+1에는 타워가있고 그 곳에 궁수가 있을 수 있음

# N이 5인경우 궁수가 있을 수 있는 경우의 수는 5C3 = 10
# 경우의수만큼 multi-BFS
enemy_list = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            enemy_list.append((i, j)) # 적 y,x 좌표 저장
            
archer_candidates = combinations(range(M), 3)

def bfs(archer: int, temp_board):
    # archer은 현재 archer가 어떤 성에 있는지를 위치 (시작 : 0) 으로 나타낸것
    dq = deque()
    
    dq.append((N-1, archer, 1)) # (y,x,current_d)
    while dq:
        y, x, current_d = dq.popleft()
        if current_d > D or x >= M or y < 0 or x < 0: # 거리가 4이상이거나 범위 벗어남? 안봄
            continue
        
        if temp_board[y][x] == 1: # 궁수의 공격으로 제거 가능
            return (y, x) # 제거한 좌표 반환
        
        dq.append((y, x-1, current_d+1))
        dq.append((y-1, x, current_d+1))
        dq.append((y, x+1, current_d+1))
        
    return (None, None) # 궁수의 공격으로 제거 불가능한 경우
    
def check_board(temp_board):
    candidate = []
    for i in range(N):
        for j in range(M):
            if temp_board[i][j] == 1:
                candidate.append((i, j))
                
                
    for candid in candidate[::-1]:
        y, x = candid
        temp_board[y][x] = 0 # 사라짐 
        
        if y+1 < N:
            temp_board[y+1][x] = 1
    
    # print(temp_board)
    for i in range(N):
        for j in range(M):
            if temp_board[i][j] == 1:
                return True
            
    return False

max_result = 0
# print(list(archer_candidates))
for a1, a2, a3 in archer_candidates:
    temp_board = deepcopy(board)
    
    result = 0
    while True:
        coord_a_li = []
        coord_a1 = bfs(a1, temp_board)
        coord_a2 = bfs(a2, temp_board)
        coord_a3 = bfs(a3, temp_board)
        
        coord_a_li.append(coord_a1)
        coord_a_li.append(coord_a2)
        coord_a_li.append(coord_a3)
        
        for coord_a_y, coord_a_x in coord_a_li:
            # print(coord_a_y, coord_a_x)
            if coord_a_y is not None: # 유효하면
                if temp_board[coord_a_y][coord_a_x] == 1:
                    temp_board[coord_a_y][coord_a_x] = 0
                    # print(coord_a_y, coord_a_x)
                    result += 1
        # print(temp_board)
        if not check_board(temp_board):
            break
        
    # print(a1,a2,a3,'|',result)                    
    max_result = max(result, max_result)                
    
                
                
print(max_result)
            

    

        