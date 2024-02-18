N = int(input())

board = [[0]*(N+1) for i in range(N+1)]
like_list = [[] for i in range(N**2 + 1)]

def check(r, c, student) -> int:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    like_count = 0
    for i in range(4):
        dr = r + dy[i]
        dc = c + dx[i]
        
        if 1 <= dr <= N and 1 <= dc <= N: # 조건
            for like in like_list[student]:
                if board[dr][dc] == like:
                    like_count += 1
    
    return like_count

def check_empty(r, c) -> int:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    empty_count = 0
    for i in range(4):
        dr = r + dy[i]
        dc = c + dx[i]
        
        if 1 <= dr <= N and 1 <= dc <= N: # 조건
            if board[dr][dc] == 0:
                empty_count += 1
    
    return empty_count
            
        
def process(student):
    # board에 student가 좋아하는 사람이 인접해 있는 개수
    info = [[-1]*(N+1) for i in range(N+1)] 
    
    
    for r in range(1, N+1):
        for c in range(1, N+1):
            # 비어있는지 체크
            if board[r][c] == 0: # 비어있다면?
                info[r][c] = check(r, c, student)
            
    # 2번 조건
    
    seats = []
    max_value = 0    
    for r in range(1, N+1):
        for c in range(1, N+1):
            # 가장 인접해 있는 칸이 많은지 체크
            if info[r][c] > max_value:
                seats = [] # 초기화
                max_value = info[r][c]
                seats.append((r, c))
            elif info[r][c] == max_value:
                seats.append((r, c))
                
                
    # 1을 만족하는 칸이 여러개이면
    if len(seats) != 1:
        max_value = 0  
        seats_apply = []
        for i in range(len(seats)):
            r, c = seats[i]
            if check_empty(r, c) > max_value:
                seats_apply = [] # 초기화
                max_value = check_empty(r, c)
                seats_apply.append((r, c))
            elif check_empty(r, c) == max_value:
                seats_apply.append((r, c))
        
        # print("info", info)
        # print("seats", seats)        
        # print("seats_apply", seats_apply) 
        target_y, target_x = seats_apply[0]
        board[target_y][target_x] = student           
            
    else:
        
    # seats[0]이 그 자리임
        # print("info", info)
        # print("seats", seats)
        target_y, target_x = seats[0]
        board[target_y][target_x] = student
            
    # print(board)

    
for i in range(N**2):
    # p, *like = input().replace(' ', '')

    # like_list[int(p)] = list(map(int, like))
    p, a,b,c,d = map(int, input().split())
    like_list[p] = [a,b,c,d]
    # print("pts:", int(p))
    process(int(p))
    

happyness = 0
def get_happyness(r, c, student):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    like_count = 1
    for i in range(4):
        dr = r + dy[i]
        dc = c + dx[i]
        
        if 1 <= dr <= N and 1 <= dc <= N: # 조건
            for like in like_list[student]:
                if board[dr][dc] == like:
                    like_count *= 10
                        
    if like_count != 1:
        return int(like_count/10)
    else:
        return 0
       


result = 0

for r in range(1, N+1):
    for c in range(1, N+1):
        result += get_happyness(r, c, board[r][c])
        
        
print(result)
        
        
# print(like_list)
# print(board)
    
    
