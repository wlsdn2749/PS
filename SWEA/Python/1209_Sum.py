
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 10 + 1):
    T = int(input())
    board = [list(map(int, input().split())) for _ in range(100)] # 100x100
    max_value = 0
    max_value_diagonal = 0
    max_value_reverse_diagonal = 0
    
    max_value_row = max([sum(board[i]) for i in range(100)])
    for i in range(100):
        max_value_diagonal += board[i][i]
        max_value_reverse_diagonal += board[i][99-i]
        
        for j in range(i): board[i][j], board[j][i] = board[j][i], board[i][j]

    max_value_col = max([sum(board[i]) for i in range(100)])
    
    print(f"#{test_case} {max(max_value_row, max_value_col, max_value_reverse_diagonal, max_value_diagonal)}")
    

    
    
    
    