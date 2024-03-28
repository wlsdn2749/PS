R, C = map(int, input().split())

board = [[] for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    board[i] = (list(input().strip()))
    
def dfs(y, x):
    if x == C-1:
        return True # 도착

    if 0 <= y < R and 0 <= x < C:
        if board[y][x] != "x" and visited[y][x] == 0:
            visited[y][x] = 1
            
            if dfs(y, x-1):
                return True
            if dfs(y, x):
                return True
            if dfs(y, x+1):
                return True
                            
    return False

    
answer = 0
for i in range(R):
    if dfs(i, 0):
        answer += 1
        
print(answer)
    
