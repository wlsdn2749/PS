
def solve():
    n, m = map(int, input().split())
    result = 0

    matrix = list()
    for i in range(n):
        matrix.append([int(c) for c in input().strip()])
    
    # print(matrix)
    for src in range(1 << n*m): # 0부터 2^(n*m)번 반복
        # 세로 계산 src & (1 << cur_idx) == 1인 경우
        total_vertical_sum = 0
        for j in range(m):
            vertical_sum = 0
            for i in range(n):
                cur_idx = i*m + j
                # print(cur_idx, src & (1 << cur_idx))
                # print(cur)
                if src & (1 << cur_idx) != 0: # 특정 비트가 1이라는것은, 2의 배수로 계산되는 값이기 때문에 0이 아니라고 판단
                    vertical_sum = 10*vertical_sum + matrix[i][j] # 현재 계산된 값에다 * 10 + 지금 값
                else: # 끊기는건 초기화
                    total_vertical_sum += vertical_sum
                    vertical_sum = 0
                    

            total_vertical_sum += vertical_sum # 계산
            # print(f"src: {src}, totalverticalsum: {total_vertical_sum}")

        # 가로 계산 src & (1 << cur_idx) == 0 인ㄱ 경우
        total_horizontal_sum = 0
        for i in range(n):
            horizontal_sum = 0
            for j in range(m): 
                cur_idx = i*m + j
                # print(f"src: {src}, cur_idx: {cur_idx} 1<< cur_idx : {1 << cur_idx} src & (1 << cur_idx): {src & (1 << cur_idx)}")
                if src & (1 << cur_idx) == 0:
                    horizontal_sum = 10*horizontal_sum + matrix[i][j]
                    # print(horitontal_sum)
                else: # 끊기는건 초기화
                    total_horizontal_sum += horizontal_sum
                    horizontal_sum = 0

            total_horizontal_sum += horizontal_sum # 계산
 
        result = max(result, total_horizontal_sum + total_vertical_sum)

    return result

print(solve())
        