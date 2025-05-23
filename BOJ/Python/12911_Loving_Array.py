def count_arrays(N, K):
    MOD = 1_000_000_007
    
    # 메모리 최적화를 위해 두 개의 행만 사용
    dp = [1] * (K + 1)  # 첫 번째 행 초기화 (1-인덱싱)
    dp[0] = 0  # 0번 인덱스는 사용하지 않음
    
    for i in range(2, N+1):
        new_dp = [0] * (K + 1)
        total_sum = sum(dp) % MOD

        # 역순으로 처리
        for j in range(K, 0, -1):
            # 초기값은 전체합
            new_dp[j] = total_sum

            # 전체합에서 배수를 빼면됨
            # 4 2인 경우 2의 입장에서 앞에 친구가 2의 배수면 안되기에, 이를 제거하면 됨.
            for x in range(2*j, K+1, j):
                new_dp[j] = (new_dp[j] - dp[x]) % MOD

        # print(dp, new_dp)
        dp = new_dp

    return sum(dp) % MOD



# 예시 실행
if __name__ == "__main__":
    N, K = map(int, input().split())
    print(count_arrays(N, K))