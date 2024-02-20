import heapq

N = int(input())

meetings = []

for i in range(N):
    start_time, end_time = map(int, input().split())
    
    meetings.append((start_time, end_time))

meetings.sort(key=lambda x:x[0]) # 끝 시간 정렬


pq = []
max_len = 0
for start_time, end_time in meetings:
    if not pq:
        heapq.heappush(pq, end_time)
        continue
    
    # 가장 작은 끝나는 시각이 입력 받을 시간 보다 크다면
    while pq and pq[0] <= start_time:
        heapq.heappop(pq)
        
    heapq.heappush(pq, end_time)
    
    max_len = max(max_len, len(pq))
        
print(max_len)
        
    
    
    


    
    