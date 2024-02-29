N, M = map(int, input().split())

car = list(map(int, input().split()))

end = max(car) * N # 모두가 탈 수 있는 최대 시간
start = 0 

sec = end

if N <= M: # 놀이기구 개수보다 사람 수가 적을떄 바로 탈 수 있음
    print(N) 
    exit(0)
    
while start <= end:
    # print(start, end)
    mid = (start + end) // 2
    
    k = 0
    
    for i in range(len(car)):
        k += ( mid // car[i]) + 1 # 최소시간 구하기  # 0번째에는 모든 학생이 타므로 +1해준다
    
    # print(k)
    if k < N: # N번째 학생이 아직 타지 못했으므로
        start = mid + 1
        
    elif k >= N: # N번째 학생이 탔으므로 최소시간 갱신
        sec = min(sec, mid)
        end = mid - 1
        
        
# 여기서 sec은 N명의 아이들이 최소시간으로 놀이기구에 탑승했다는것을 의미함
        
# 바로 전에 탄 아이들이 몇 명인가?
prev_n = 0
for i in range(len(car)):
    prev_n += ((sec-1) // car[i]) + 1
    
# sec에 탈 수 있으면 prev_n +=1
cur_n = prev_n

for i in range(len(car)):
    if sec % car[i] == 0: # 그 시간대에 i번째 놀이기구를 탑승했으면
        cur_n += 1 # 현재 번호 증가
        
    if cur_n == N: # N번째 아이가 탑승했다면
        print(i+1)
        break
    
    
# print(sec)
    