from collections import deque, defaultdict


N, d, k, c = map(int, input().split())


rotating_sushi = list()

sushi_dq = deque()
sushi_dict = defaultdict(int) # 기본으로 0값 입력

for i in range(N):
    rotating_sushi.append(int(input()))
    
rotating_sushi.extend(rotating_sushi[:k-1]) # 회전초밥이니까 마지막~k-1개까지 더 먹을 수 있음

sushi_max = 0

def get_sushi_dict_len():
    count = 0
    
    for k, v in sushi_dict.items():
        if v != 0:
            count += 1
            
            
    return count
        
for i in range(len(rotating_sushi)): # 초밥 동안에
    
    cur_sushi = rotating_sushi[i]
    
    if len(sushi_dq) < k: #아직 연속으로 k개 안먹었다면
        
        sushi_dq.append(cur_sushi) # 현재 연속으로 먹은 초밥 개수라고 append
        sushi_dict[cur_sushi]+=1 # 먹은 초밥 기록
        
        if len(sushi_dq) == k:
            if sushi_dict[c] == 0 :# 쿠폰으로 먹을 수 있는 초밥이 dict에 없다면
                sushi_max = max(get_sushi_dict_len() + 1, sushi_max)
            else: # 그냥 유지
                sushi_max = max(get_sushi_dict_len(), sushi_max)
        else:
            sushi_max = max(get_sushi_dict_len(), sushi_max)

    
    elif len(sushi_dq) == k : # 지금 k개 꽉찼다면
        popped_sushi = sushi_dq.popleft() # 왼쪽에서 초밥 하나 빼고
        
        sushi_dict[popped_sushi] -= 1 # 초밥 제거
        
        sushi_dq.append(cur_sushi) # 현재 연속으로 먹은 초밥 개수라고 append
        
        sushi_dict[cur_sushi] += 1 # 초밥 추가
        
        if sushi_dict[c] == 0 :# 쿠폰으로 먹을 수 있는 초밥이 dict에 없다면
            sushi_max = max(get_sushi_dict_len() + 1, sushi_max)
        else: # 그냥 유지
            sushi_max = max(get_sushi_dict_len(), sushi_max)
    
    # print(sushi_max)
    # print(sushi_dq)
    # print(sushi_dict)
            
            
    
print(sushi_max)
    


    
    
    
    