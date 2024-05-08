def solution(food_times, k):
    idx = 0 # 순회하면서 체크하는 변수
    time = 0 # 시간 
    no_food_cnt = 0 # 섭취해야할 음식이 없을 경우 다음으로 넘어가며 카운트 증가 
    
    while time <= k:
            
        # 섭취해야할 음식이 없을 경우 다음 idx를 순회    
        if food_times[idx%len(food_times)] == 0:
            
            idx += 1
            no_food_cnt += 1
            
            # 모두 순회했는데, 섭취해야할 음식이 없을 경우 -1 리턴
            if no_food_cnt == len(food_times):
                return -1
            continue
                
    
        else:
            food_times[idx%len(food_times)] -= 1
            
        # k초 이후에 어떤 음식을 섭취해야하는지
        # 만약 이때 섭취해야할 음식이 전혀 없으면 위에서 early return
        if time == k:
            return idx % len(food_times) + 1
        
        time += 1
        idx += 1
        no_food_cnt = 0