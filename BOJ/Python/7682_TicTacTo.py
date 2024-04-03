# 3x3 Game board
# 첫번째가 X, 두번째가 O

# XXX XOX
# OO. OXO
# XXX XOX
 
# 게임판이 가득찼을때
# "X가 5개, O가 4개"가 아니면 Invalid

# --- First
# "X가 O보다 1개 더 많지 않으면 Invalid"

# --- Second
# 상하좌우 대각선 탐색 (상하), (좌우), (3,9), (11,5) -> 같은 방향으로 3개 탐색하면 각 XO마다 완성 스택 증가

# --- XO스택 Case
# X 또는 O가 한개 이거나 두개 인경우, (3개는 있을 수 없음) -> Valid
# X, O가 각각 1개 인경우 -> Invalid

# 012
# 345
# 678

from itertools import combinations

def is_tictacto(a,b,c):
    
    tictacto_copyprint = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    arg_list = sorted([a,b,c])
    
    if arg_list in tictacto_copyprint:
        return True
    return False

def func(combination: combinations, visited) -> int:

    count = 0

    for a,b,c in combination:
        if is_tictacto(a,b,c):
            if not visited[a]: visited[a] = True   
            else: continue
            if not visited[b]: visited[b] = True
            else: continue
            if not visited[c]: visited[c] = True
            else: continue
        
            count += 1
    
    return count

while (case := input()) != "end":
    visited = [False for _ in range(9)]
    X_list, O_list = [], []
    X_completion, O_completion = [], []
    X_count, O_count = 0, 0
    
    for idx, c in enumerate(case):
        if c == "X":
            X_list.append(idx)
        elif c == "O":
            O_list.append(idx)
    
    X_combintations = combinations(X_list, 3)
    O_combintations = combinations(O_list, 3)
    
    X_count = func(X_combintations, visited)    
    O_count = func(O_combintations, visited)
    
    # print(X_count, O_count)
    if len(X_list) < len(O_list):
        print("invalid")
        continue
    
    if abs(len(X_list) - len(O_list)) >= 2:
        print("invalid")
        continue
    
    if X_count >= 2 or O_count >= 2:
        print("invalid")
    
    elif X_count == 1 and O_count == 1:
        print("invalid")
    
    elif O_count == 1 and len(O_list) != len(X_list):
        print("invalid")
        
    elif X_count == 1 and len(X_list) - len(O_list) != 1:
        print("invalid")
        
    elif X_count == 0 and O_count == 0:
        if len(X_list) + len(O_list) == 9 and len(X_list) - len(O_list) == 1: # Full
            print("valid")
            continue
        else:
            print("invalid")
            continue
        
    else:
        print("valid")
    
    
    
            
    
            
    
    
    
    
    
    
    
    




