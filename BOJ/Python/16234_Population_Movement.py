def find(a: int):
    if pts[a] == a:
        return a
    
    pts[a] = find(pts[a])
    return pts[a]

def union(a:int, b:int):
    pts_a = find(a)
    pts_b = find(b)
    
    pts[pts_b] = pts_a # b의 부모를 a와 같게!
    
def compare(a, b):
    return abs(countrys[a] - countrys[b])

def open_gate(a, b):
    # print(a,b)
    if L <= compare(a, b) <= R: # 국경선이 열린다면
        union(a,b) # a와 b를 union
        
def movement_process():
    result_list = [[] for _ in range(N**2)]
    
    movement_available = False
    for i in range(N**2):
        result_list[find(pts[i])].append(i) # 같은 연합일경우 인덱스를 같이 넣음 # find를 굳이해줘야하나..?
        
    for result in result_list:
        if len(result) == 1: # 연합이 없는 경우는 continue
            continue
        
        elif len(result) >= 2: # 연합이 있는 경우?
            movement_available = True # 일단 이동은 함
            movement_people = sum([countrys[idx] for idx in result]) # 연합의 인구수
            
            for idx in result: # 이동
                countrys[idx] = movement_people // len(result)
                
    return movement_available


if __name__ == "__main__":
    
    N, L, R = map(int, input().split())

    countrys = [] # 1차원 배열로 해결 가능?

    movement = True
    count = -1
    
    # 인구값 입력
    for i in range(N):
        [countrys.append(k) for k in map(int, input().split())]
            
    while movement:
        count += 1
        pts = [i for i in range(N**2)] # 0번부터 시작
        
        # 가로 국경선 확인
        for i in range(N**2-1):    
            if (i+1) % N != 0:
                open_gate(i, i+1)
                
        # 세로 국경선 확인
        for i in range(N**2-N):
            open_gate(i, i+N)
            
        
        movement = movement_process() # 이동 했는지 안했는지 여부, 안했으면 여기서 끝남
        
        # print(countrys)
        
    print(count)
2