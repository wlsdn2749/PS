import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
f_answer = []
for test_case in range(1, T + 1):
    num = input().strip()
    
    def backtracking(cur_num, num):
        if not num:
            return cur_num
        
        cur_num += int(num[0])
        answer = backtracking(cur_num, num[1:])
        
        if answer >= 10:
            answer = backtracking(0, list(str(answer)))
            
        return answer
    
    answer = backtracking(0, num)
    f_answer.append(f"#{test_case} {answer}")
    
for ans in f_answer:
    print(ans)
    

    
        
