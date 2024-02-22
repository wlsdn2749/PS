from collections import deque

N = int(input())

arr = list(map(int, input().split()))

result = [0 for _ in range(len(arr))]

st = deque()

for i in range(len(arr)):
    
    element = arr[i]
    
    if not st: # stack이 비어 있으면
        result[i] = 0 # 송신 못함
        st.appendleft((element, i+1)) # (높이와, 순서) 저장
        continue
    
    while st and st[0][0] < element: # stack에 원소가 존재하고, 입력되는 element보다 작은게 없을때까지 pop, (송신 되는 탑이 있으면 멈춤)
        st.popleft()
        
    # 만약 st가 여전히 있다면 
    
    # top에 있는 원소는 입력으로 들어가는 top을 송신할 수 있음
    
    # 그리고 내림차순을 정렬을 위해 push
    if st:
        top_order = st[0][1] 
        result[i] = top_order
        st.appendleft((element, i+1))
        
    # 만약 st가 존재하지 않는다면 송신 못하므로
    else:
        result[i] = 0
        st.appendleft((element, i+1)) # (높이와, 순서) 저장


print(*result)        
        
        
    
    