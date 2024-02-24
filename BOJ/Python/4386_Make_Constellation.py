N = int(input())

pts = [i for i in range(N+1)]

def find(a: int) -> int:
    if pts[a] == a: # 자기자신을 가리키는 pts 배열이면 리턴
        return a
    
    pts[a] = find(pts[a]) # path compression
    return pts[a]       
    
def union(a: int, b: int) -> bool:
    pts_a = find(a)
    pts_b = find(b)
    
    # 부모가 이미 같으면 cycle이라고 판단
    if pts_a == pts_b:
        return False
    else:
        pts[pts_b] = pts_a # b의 부모를 a와 같게 만듬 (작은 쪽 union)
        return True
    
    
stars = []
for i in range(1, N+1): # i번째, 1부터 시작
    x, y = map(float, input().split())
    
    stars.append((i,x,y)) # i번째 별은 (x,y) 좌표에 있음
    
distances = []

for j in range(len(stars)):
    for i in range(j): # (i, j, cost) -> output
        order1, x1, y1 = stars[i]
        order2, x2, y2 = stars[j]
        distance = ((x1-x2)** 2 + (y1-y2)**2) ** 0.5
        
        distances.append((order1, order2, distance))
        

distances.sort(key=lambda x:x[2]) # distance 기준 오름차순

result = 0

for info in distances:
    
    order1, order2, distance = info
    
    if union(order1, order2):
        result+=distance
        
print(result)
         
    
        
        
        
        
    
    
    
    