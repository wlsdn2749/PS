dp = [[ 0 for _ in range(10)] for _ in range(12)]

# 0번은 안씀
# 1~9까지, 각 행은 앞자리를 나타내고
# 1~9까지, 각 열은 숫자의 자리수를 나타냄

dp[1][0] = 1

for i in range(1, 11):
    
    for j in range(1, 10):
        if i == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = sum(dp[i-1][0:j-1+1])


# [print(dp[i]) for i in range(12)]

# 여기서 dp는 이미 구함

def check_range(number, l, r):
    if l < number <= r:
        return True
    
    return False

def get_limit(cur_num):

    while cur_num > 10:
        right = cur_num % 10
        cur_num = cur_num // 10
        left = cur_num % 10
        # print("left, right: ", left, " ",right)
        if left <= right:
            return False
        
    return True
    
def get_number(pos, i, j, prev_range) -> int:
    # 자리수가 i이면서, 앞자리가 j인 경우,
    # 이 조건을 만족하는 제일 작은 수는 prev_range+1임
    # 앞에 j 고정두고

    start = j * 10 ** (i-1)
    cur_pos = prev_range 
    # print("curr_range", prev_range)

    if start <= 10 and i == 1:
        return prev_range 
    

    if cur_pos == pos:
        return cur_num
    
    # print("start: ", start, "end: ", )
    for cur_num in range(start, j*10**(i)):
        
        # print("cur_num, cur_pos pos", cur_num, cur_pos, pos)
        # 조건 만족하면?
        if get_limit(cur_num):
            # print("cur_num, cur_pos pos", cur_num, cur_pos, pos)
            cur_pos += 1
            if cur_pos == pos:
                return cur_num        
    
def solve(number: int) -> int:
    result = [-1]  # 결과값 저장용(리스트로 감싸서 참조 유지)
    cnt = [0]      # 몇 번째 숫자인지 카운트

    def dfs(pos, length, num):
        if result[0] != -1:
            return

        if pos == length:
            cnt[0] += 1
            if cnt[0] == number:
                result[0] = num
            return

        # 이전 자리보다 작은 수만 다음 자리에 올 수 있음
        last_digit = num % 10 if num > 0 else 10
        for next_digit in range(last_digit - 1, -1, -1):
            dfs(pos + 1, length, num * 10 + next_digit)
            if result[0] != -1:
                return

    # 한 자리수부터 최대 10자리까지 반복
    for length in range(1, 11):
        for first_digit in range(1, 10):
            dfs(1, length, first_digit)
            if result[0] != -1:
                return result[0]

    return -1




if __name__ == "__main__":
    number = int(input())
    # for i in range(1, 1000):
    print(solve(number))
    # print(solve(90))