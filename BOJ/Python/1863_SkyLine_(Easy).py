from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    
    buliding_states = []
    st = deque()
    
    for _ in range(n):
        x, y = map(int, input().split())
        buliding_states.append((x,y))
    
    buliding_states.sort(key=lambda x:x[0])
    
    cnt = 0
    for idx, (_, y) in enumerate(buliding_states):
        
        if y == 0:
            cnt += len(st)
            st.clear()
            continue
            
        while st and y <= st[-1]:
            if y == st[-1]: break
            st.pop()
            cnt+=1
            
        else:
            st.append(y)
        
        if idx == n-1: # 마지막, 0은 제거해야함
            cnt += len(st)
              
    print(cnt)
