# Matching System

# 매칭 가능한 방이 없다면
    # 새로운 방 생성 후 입장, 
    
# 처음 입장한 플레이어 기준으로 +- 10 입장 가능

# 입장 가능한 방이 있다면 입장 시킨후, 방의 정원이 모두 찰 때까지 대기시킨다.
    # 이때 가능한 방이 여러개면 가장 먼저 생성된 방에 입장한다.
    # 방의 정원이 가득 차면 게임을 시작한다
    
rooms = [] # (level, id) 

p, m = map(int, input().split())

for i in range(p):
    l, n = input().split()
    l = int(l)
    
    for idx, room in enumerate(rooms):
        if room and len(room) < m: # 방의 정원이 가득차지 않아야함
            if abs(room[0][0] - l) <= 10: # 처음 플레이한 플레이어 기준으로 +- 입장 가능
                rooms[idx].append((l, n))
                break
                
    # 매칭 가능한 방이 없다면 새로운 방 생성 후 입장    
    else:
        rooms.append([(l, n)]) 
    

for idx, room in enumerate(rooms):
    if len(room) == m:
        print("Started!")
        [print(l, n) for l, n in sorted(room, key=lambda x:x[1])]
    
    else:
        print("Waiting!")
        [print(l, n) for l, n in sorted(room, key=lambda x:x[1])]
        
            
            