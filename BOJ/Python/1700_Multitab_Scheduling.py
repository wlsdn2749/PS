N, K = map(int, input().split())

tab = [0 for _ in range(N)]

orders = list(map(int, input().split()))

count = 0
for idx, order in enumerate(orders):
    
    flag = False
    # 이미 꽂아져 있으면 스킵
    for i in range(len(tab)):
        if tab[i] == order:
            flag = True
            break
    
    if flag:
        continue
    
    # 빈칸인 경우, 자리에 할당후 스킵
    for i in range(len(tab)):
        if tab[i] == 0:
            flag = True
            tab[i] = order
            break
            
    if flag:
        continue
    
    # 멀티탭이 가득 차 있는 경우
        # 멀티탭에 이미 꽂아져 있는 것들이 뒤에 나오는지 판단
            # 현재 idx 기준 멀티탭에 꽂아져 있는 i번째가 가장 늦게 언제 나오는지를 기록
            # 가장 늦게 나오는 멀티탭에 꽂아져 있는 i번째를 (교체)
            
        # 멀티탭에 이미 꽂아져 있는 것 중 뒤에 안나오는 경우
            # 이를 바로 교체
        
        # 멀티탭에 이미 꽂아져 있는 것 중 모두가 뒤에 안나오는 경우
            # 첫번째를 교체
    
    waiting_list = []
    
    for i in range(len(tab)):
                
        for j, e in enumerate(orders[idx+1:], start=idx+1):

            if e == tab[i]:
                waiting_list.append((i, j)) # i번째 꽂혀 있는 전자기기가, j번째에 나옴
                break
            
        else:
            tab[i] = order
            count+=1
            break
        
    else:
        waiting_list.sort(key=lambda x:-x[1])
        tab[ waiting_list[0][0] ] = order
        count+=1

print(count)
         
        
        

                
        
    
        
    
    