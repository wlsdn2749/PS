



def solve():
    N = 6
    board = [ list(map(int, input().split())) for _ in range(N)] # 6x6

    # 4x3 , 3x4 체크
    # [start_x:start_x+4], [start_y:start_y+3] Check 가로, 세로
    # 가로 방향으로 순회 하면서, 1x4x1인지 확인
    def get_4x3(start_x, start_y): 
        
        if start_x+3 >= N or start_y+2 >= N:
            return False
        
        trace = []
        for y in range(start_y, start_y+3):
            count = 0
            for x in range(start_x, start_x+4):
                if board[x][y] == 1:
                    count += 1
            trace.append(count)

        if trace == [1,4,1]:
            return True
        
        return False
    
    def get_3x4(start_x, start_y):
        if start_x+2 >= N or start_y+3 >= N:
            return False
        
        # print(start_x, start_y)
        trace = []
        for x in range(start_x, start_x+3):
            count = 0
            for y in range(start_y, start_y+4):
                if board[x][y] == 1:
                    count += 1
            trace.append(count)

        if trace == [1,4,1]:
            return True
        
        return False


    for y in range(N):
        for x in range(N):
            if get_3x4(x, y) or get_4x3(x, y):
                return True
            
    return False


if __name__ == "__main__":
    P = 3
    for i in range(P):
        if solve():
            print("yes")
        else:
            print("no")


"""
0 0 0 0 1 0
0 0 0 1 1 1
0 0 0 0 1 0
0 0 0 0 1 0
0 0 0 0 0 0
0 0 0 0 0 0
0 1 1 0 0 0
0 1 0 0 0 0
0 1 0 0 0 0
1 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 1 1 0
0 0 1 1 0 0
0 0 0 1 1 0
0 0 0 0 0 0
0 0 0 0 0 0
"""