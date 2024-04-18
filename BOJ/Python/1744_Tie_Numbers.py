# 정렬도 필요없음
# 우선순위큐
'''
    -1, 1, 2, 3, 4
    마이너스는 마이너스 끼리
    플러스는 플러스끼리
    
    1은 미리 제거해서 더하고 
    
    마이너스가 짝수 개일경우
    마이너스끼리 곱해서 +를 만들되
    마이너스의 절댓값이 큰 것끼리 서로 곱함
    -7 -6 -4 - = 7x6 + 4*2
    
    마이너스가 홀수 개일경우
    마이너스의 절댓값이 큰 것끼리 서로 곱하고
    남은건 그대로 쓰되.
    0이 있다면 곱해서 0을 만들기
    
    플러스는
    절댓값이 큰 것끼리 곱하기    
    
'''

import heapq

N = int(input())

minus_pq = []
plus_pq = []
zero_q = []
result = 0

for _ in range(N):
    num = int(input())
    
    if num == 0:
        zero_q.append(0)
    
    elif num == 1: # 1은 미리 제거
        result += 1
        
    elif num < 0:
        heapq.heappush(minus_pq, num)
        
    elif num > 0:
        heapq.heappush(plus_pq, -num)
    

cur_process = 1
while minus_pq:
    
    if cur_process == 1:
        num = heapq.heappop(minus_pq)
        cur_process *= num
    
    else:
        num = heapq.heappop(minus_pq)
        cur_process *= num
        result += cur_process
        cur_process = 1
        
# 마이너스 갯수가 홀수 개 인 경우
if cur_process != 1: 
    # 0 이 없다면
    if not zero_q:
        result += cur_process # 그대로 더함

cur_process = 1    
while plus_pq:
    if cur_process == 1:
        num = -heapq.heappop(plus_pq)
        cur_process *= num
    
    else:
        num = -heapq.heappop(plus_pq)
        cur_process *= num
        result += cur_process
        cur_process = 1
        
if cur_process != 1:
    result += cur_process


print(result)