from collections import deque

N = int(input())

arr = list(map(int, input().split()))

result = [0 for _ in range(len(arr))]

st = deque()

for i in range(len(arr)-1, -1, -1): # 역순 탐색
    
    value = arr[i]
            
    while st and value >= st[0] : # value가 top보다 작을때까지 반복 # case 1 : 9면 8을 빼야함 # case 2 : 2여도 2는 뺌
        st.popleft()
        
    if not st: # 스택이 비어있다면
        result[i] = -1
        
    if st: # 만약 스택이 있다면?
        result[i] = st[0]
        
    st.appendleft(value)
        
        
print(*result)
        
        
        
        
    
        
        



