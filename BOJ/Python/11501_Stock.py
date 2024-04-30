import sys
input = sys.stdin.readline

if __name__ == "__main__":
    
    T = int(input())
    
    for test_case in range(T):
        N = int(input())
        li = list(map(int, input().split()))
        
        cur_max = 0
        profit = 0
        for value in li[::-1]:
            
            if cur_max < value: # 원하는 만큼 주식을 판다
                cur_max = value
                continue
            
            if cur_max > value:
                profit += cur_max - value # 차익
                
                
        print(profit)
                
            
            