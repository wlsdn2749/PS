'''
    a -> b 입력,
    a 기준 오름 차순 정렬
    1 6 
    8 12
    13 17
    
    웅덩이
    1->5
    8->11
    13->16
    
    1 2 3 / 4 5 6
    
    8 9 10 / 11 12 13
    14 15 16 /
    
    start -> end
    1 -> 3
    end가 아직 5에 도달하지 않았음
    4 -> 6
    end가 5보다 큼 종료
    
    - 마지막 장판 6이 8보다 작으므로
    - start의 갱신은 없음
    
    
    start -> end
    8 -> 10
    end가 아직 12에 도달하지 않았음
    11 -> 13 
    13이 12보다 큼 종료
    
    마지막이 13이였는데
    현재 스타트가 13이므로 이는 포함,
    현재 스타트를 14로 변경 
    14 -> 16
    16이 16보다 크거나 같으므로 종료 
    -> 5
'''

N, L = map(int, input().split())

pools = [tuple(map(int, input().split())) for _ in range(N)] # (start, end)
pools.sort(key=lambda x:x[0])

counts = 0
last_start = -1

for pool in pools:
    start, end = pool
    
    if last_start >= start:
        start = last_start
        
    while start <= end-1: # end는 1 6인 경우 (1 5)
        
        start += L # 널빤지 만큼 증가
        
        counts += 1
    else:
        last_start = start

print(counts)
        
    
