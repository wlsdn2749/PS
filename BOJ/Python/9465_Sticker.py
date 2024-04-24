import sys
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    
    for test_case in range(T):
        
        dp = []
        
        n = int(input())
        
        for i in range(2):
            dp.append(list(map(int, input().split()))) # dp[0]은 첫 번째 줄
        
        if n != 1: # 1 인경우는 바로 출력
            
            dp[0][1] += dp[1][0]
            dp[1][1] += dp[0][0] # 두 번째까지 미리 계산
            
            for i in range(2, n): # 세 번째 부터 시작
                
                dp[0][i] += max(dp[1][i-1], dp[1][i-2]) # 이웃하지 않은 대각선이거나, 그 옆
                dp[1][i] += max(dp[0][i-1], dp[0][i-2]) # 마찬가지
            
        # print(dp)
        print(max(dp[0][n-1], dp[1][n-1]))
            
            
        
            
            