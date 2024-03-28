R, C = map(int, input().split())

board = [[] for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    board[i] = (list(input().strip()))
    
def dfs(y, x):
    if x == C-1:
        return True # 도착

    dy = [-1, 0, 1]
    for i in range(3):
        ddx = x+1
        ddy = y + dy[i]
        if 0 <= ddy < R and 0 <= ddx < C:
            if board[ddy][ddx] != "x" and visited[ddy][ddx] == 0:
                visited[ddy][ddx] = 1
                
                if dfs(ddy, ddx):
                    return True
                            
    return False

answer = 0
for i in range(R):
    if dfs(i, 0):
        answer += 1
        
print(answer)
    
