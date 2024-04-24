import sys

input = sys.stdin.readline
    
if __name__ == "__main__":
    N = int(input())
    
    states = []
    
    for _ in range(N):
        X, A = map(int, input().split())
        states.append((X,A))
        
    states.sort(key=lambda x:x[0]) # 마을 기준 오름차순 정렬
    
    all_villagers = sum(map(lambda x: x[1], states))
    
    cur_villagers = 0
    answer = 0
    for x, a in states:
        cur_villagers += a
        
        if cur_villagers >= (all_villagers + 1) // 2:
            answer = x
            break
        
    
    print(x)
        
        
    

    