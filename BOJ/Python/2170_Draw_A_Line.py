import sys
input = sys.stdin.readline

N = int(input())

lines = []

def valid_lines(left, right):
    
    for i in range(len(lines)):
        lines_left, lines_right = lines[i]
        
        # 새로 들어온 라인이 기존에 있는 선의 범위를 넘어갈 경우
        if right < lines_left or lines_right < left:        
            continue 
        
        # 어떻게든 포함되는 경우
        # 그 위치의 좌표를 확장(갱신)
        else:
            lines[i] = (min(left, lines_left), max(right, lines_right))
            return
        
    # 현재 모든 lines에 포함되어 있지 않은 경우
    lines.append((left, right))
            
li = []
for i in range(N):
    left, right = map(int , input().split())
    li.append((left, right))

li.sort(key=lambda x:x[0])
    
    
for i in range(len(li)):
    valid_lines(li[i][0], li[i][1])
    
# print(lines)
print(sum([i[1] - i[0] for i in lines]))
    
    
    

        
            
            
            
    
