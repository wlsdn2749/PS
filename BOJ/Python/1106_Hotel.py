C, N = map(int, input().split())

dp = [1e8 for _ in range(C+100)]
dp[0] = 0

bldgs = []

for _ in range(N):
    bldgs.append(tuple(map(int, input().split()))) # cost, people
    
for idx, (cost, people) in enumerate(bldgs):
    for i in range(people,C+100): # num_people 부터 C+100 까지 반복
        dp[i] = min(dp[i-people]+cost, dp[i]) # i명일 때, 최소비용 갱신
        
print(min(dp[C:]))