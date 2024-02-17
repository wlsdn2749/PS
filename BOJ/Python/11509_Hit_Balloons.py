import bisect

N = int(input())

li = list(map(int, input().split()))

arrows_list = [0 for i in range(1000001)]

result = 0
for i in li:
    if arrows_list[i] > 0: # 화살이 이미 있다면 (그 화살이 내려감 )
        arrows_list[i] -= 1 # 화살 하나 빼고
        arrows_list[i-1] += 1 # h-1 위치 화살 하나 더해주고
    else: # 화살이 없는 경우 (맞추고 하나 뺌)
        arrows_list[i-1] += 1
        result += 1

print(result)
    
    
        
    
    

