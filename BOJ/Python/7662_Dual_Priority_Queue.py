import heapq

test_case = int(input())

for T in range(test_case):
    max_heap = []
    min_heap = []
    k = int(input())
    # 0이 기본값
    # 현재 0이라는 것은 Queue에 없다는 뜻
    check_order = [0 for _ in range(1_000_001)]
    indice = -1
    for i in range(k):
        a, b = input().split()
        
        if a == 'I': # Insert
            indice += 1 # 삽입될 때 마다 indice가 증가
            check_order[indice] = 1 # 삽입됬다고 표시
            heapq.heappush(max_heap, (-int(b), indice))
            heapq.heappush(min_heap, (int(b), indice))

        elif a == 'D' and max_heap and min_heap: # Delete
            if b == '1': # 최댓값 삭제
                while max_heap:                    
                    _, order = heapq.heappop(max_heap)
                    if check_order[order] == 0: # 제거했는데 이미 큐에 없으면? (최소값에 의해 빠졌으면)
                        continue
                    
                    else: # 제거했는데 큐에 있는거라면
                        check_order[order] = 0
                        break
                
            elif b == '-1': # 최소값 삭제
                while min_heap:                    
                    _, order = heapq.heappop(min_heap)
                    if check_order[order] == 0: # 제거했는데 이미 큐에 없으면? (최대값에 의해 빠졌으면)
                        continue
                    
                    else: # 제거했는데 큐에 있는거라면
                        check_order[order] = 0
                        break
        
    
    max_value = None
    min_value = None
    
    while max_heap:
        value, order = heapq.heappop(max_heap)
        
        if check_order[order] == 0: # 제거했는데 이미 큐에 없으면? (최소값에 의해 빠졌으면)
            continue
        
        else: # 제거했는데 큐에 있는거라면            
            max_value = -value
            break

    while min_heap:
        value, order = heapq.heappop(min_heap)
        
        if check_order[order] == 0: # 제거했는데 이미 큐에 없으면? (최소값에 의해 빠졌으면)
            continue
        
        else: # 제거했는데 큐에 있는거라면            
            min_value = value
            break
        
        
    if max_value == None or min_value == None:
        print("EMPTY")
    else:
        print(max_value, min_value)

