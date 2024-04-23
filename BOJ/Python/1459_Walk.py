X, Y, W, S = map(int, input().split())

origin_X, origin_Y = int(repr(X)), int(repr(Y))
result_a = 0
result_b = 0


min_xy = min(X,Y)
result_a += min_xy * S # 확정
X -= min_xy
Y -= min_xy

if X == 0:
    if Y % 2: # 홀수
        result_a += W 
        Y -= 1  

if Y == 0:
    if X % 2: # 홀수
        result_a += W
        X -= 1
        
result_a += min( max(X, Y) * S, max(X, Y) * W)
    

result_b += (origin_X+origin_Y)*W
# print(result_a)
# print(result_b)

if result_a != 0:
    print(min(result_a, result_b))
else:
    print(result_b)
    
    

