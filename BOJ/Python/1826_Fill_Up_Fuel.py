import sys
input = sys.stdin.readline

N = int(input())

gas_station = []

for _ in range(N):
    a, b = map(int, input().split())
    gas_station.append([a,b,False]) # 시작점에서 위치, 가스 충전량, 방문 여부
    
gas_station.sort(key=lambda x:x[0])

L, P = map(int,input().split())


count = 0
cur_list = []
search_idx = 0

while True:
    
    if P >= L: # 마을까지 도달 가능한 경우
        print(count)
        break
    
    if count >= N: # 모든 경우를 다 탐색 했는 데도 도달 불가능한 경우
        print(-1)
        break
    
    while True:
        if search_idx >= N:
            break
        
        a,b,visited = gas_station[search_idx]
        
        if a <= P:
            cur_list.append([a, b, visited]) # 인덱스
            search_idx += 1
        else:
            break
        
    max_fuel = 0
    visited_index = 0
    # print(cur_list)
    
    for i in range(len(cur_list)):
        a,b,visited = cur_list[i]
        
        if visited:
            continue
        
        if max_fuel < b: 
            max_fuel = b 
            visited_index = i
            
    
    if max_fuel:
        cur_list[visited_index][2] = True # 방문처리 
        P += max_fuel
        count += 1
    
    if max_fuel == 0: # 현재 갈 수 있는 거리를 모두 탐색헀는데, 더 이상 갈 수가 없으므로 마을에 도착 불가
        print(-1)
        break

