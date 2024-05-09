from itertools import combinations

def check():
    dx = [1, 0, -1, 0] # 동남서북
    dy = [0, 1, 0, -1]
    
    possible_surveillance = set()
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'T':
                for r in range(4):
                    m = 1
                    temp_list = []
                    
                    while True:
                        ddy = i + dy[r] * m
                        ddx = j + dx[r] * m
                        
                        
                        # print(ddy,ddx)
                        if 0 <= ddx < N and 0 <= ddy < N:
                            
                            if board[ddy][ddx] == 'T': # 선생님이 이미 있는 경우 필요없음
                                break
                            
                            if board[ddy][ddx] == 'S': # 학생이 있는 경우
                                possible_surveillance.update(temp_list) # 싹 더해줌
                                # print(temp_list)
                                break
                                
                            m += 1
                            temp_list.append((ddy, ddx))
                            
                        else:
                            break
    
    if len(possible_surveillance) < 3: # 예외
        for i in range(N):
            for j in range(N):
                if board[i][j] == 'X':
                    possible_surveillance.add((i, j))
                    
    return possible_surveillance

def student_check_func(possible_surveillance_lst):

    student_lst = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'S':
                student_lst.append((i, j))
                
    for item in possible_surveillance_lst:
        temp_board = board.copy()
        for y, x in item:
            temp_board[y][x] = 'O' # 헀다가                
            
        if student_check(student_lst, temp_board):
            return True
        
        for y, x in item:
            temp_board[y][x] = 'X' # 풀기
    
    return False

def student_check(student_lst, temp_board):
    dx = [1, 0, -1, 0] # 동남서북
    dy = [0, 1, 0, -1]
    
    for student in student_lst:
        stu_y, stu_x = student # 현재 학생위치
        
        for r in range(4):
            m = 1
            while True:
                ddy = stu_y + dy[r] * m
                ddx = stu_x + dx[r] * m
            
                if 0 <= ddx < N and 0 <= ddy < N:
                    
                    if temp_board[ddy][ddx] == 'O':
                        break
                        
                    if temp_board[ddy][ddx] == 'T': # 불가능
                        return False
                    
                    m+=1
                else:
                    break
                    
    return True
    
def solution():
    possible_surveillance = check() # 빈칸을 놓는 후보
    possible_surveillance_lst = list(combinations(possible_surveillance, 3))
    
    # print(possible_surveillance_lst)
    if student_check_func(possible_surveillance_lst):
        return "YES"
    else:
        return "NO"                
                

if __name__ == "__main__":
    N = int(input())
    
    board = []
    for _ in range(N):
        board.append(list(map(str, input().split())))
        
    print(solution())
    