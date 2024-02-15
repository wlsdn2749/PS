N, M = map(int, input().split())

memory_list = [0] + list(map(int, input().split()))
cost_list = [0] + list(map(int, input().split()))

max_cols = sum(cost_list)
dp = [[0 for _ in range(max_cols+1)] for _ in range(N+1)]
result = max_cols # 열이 가질 수 있는 최대값

for i in range(1, N+1):
    memory = memory_list[i]
    cost = cost_list[i]
    
    for j in range(0, max_cols + 1): # 0이 여러개 있을 수 있음
        if j < cost: # 이전의 dp를 갱신
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(memory + dp[i-1][j-cost],
                           dp[i-1][j]) 
            # 현재 앱을 끈거 + 전에 잇던 DP에 그 코스트만큼 감소된것 
            # 과 바로 직전의 코스트와 비교해서 가장 큰 것
        if dp[i][j] >= M: # M보다 큰것중에 
            result = min(result, j) # 작은 코스트를 가질 수 있는 애가 result
            
            
if M != 0:
    print(result)
else:
    print(0)