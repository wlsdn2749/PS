from collections import defaultdict

N = int(input().strip())

dd = defaultdict(int)
all_num_divisors_lst = []


# 모든 약수를 구하기: 일단 include(SQRT(N))까지 돈다음에, 나눠지면, 그 몫과 함께 약수 리스트에저장
def get_all_divisors(num: int) -> list:
    divisors_lst = []
    for i in range(1, int(num**0.5)+1): 
        if num%i == 0:
            divisors_lst.append(i)
            if num//i != i:
                divisors_lst.append(num//i)

    return divisors_lst

for i in range(N):
    num = int(input().strip())
    # num을 defaultdict값에 추가
    dd[num]+=1
    all_num_divisors_lst.append(get_all_divisors(num))

print(all_num_divisors_lst)
for divisors in all_num_divisors_lst:
    answer = 0
    for divisor in divisors:
        answer += dd[divisor]
 
    print(answer-1) # 자기 자신 제거

    

    
    