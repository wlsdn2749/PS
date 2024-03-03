import sys 
input = sys.stdin.readline


while True:
    try:
        x = int(input()) # 너비

        x = x * 10_000_000 # 나노미터로 환산

        N = int(input()) # 갯수

        arr = [] # 길이를 담는 배열
        for i in range(N):
            arr.append(int(input()))
            
        arr.sort() # 오름차순 정렬 

        # 이분 탐색 O(n * log(n))

        find = False
        
        for i in range(N-1):
            
            a = arr[i]    
            
            start = i+1
            end = N-1
            
            while start <= end:
                
                mid = (start + end) // 2
                b = arr[mid]
                
                if a + b == x: # 일치
                    print('yes', a, b)
                    find = True
                    break
                elif a + b > x: # a+b가 찾고자하는 값 x보다 큰 경우 b를 낮춤 ( mid 기준 왼쪽 탐색 )
                    end = mid-1
                elif a + b < x: # a+b가 찾고자하는 값 x보다 작은 경우 b를 키움 ( mid 기준 오른쪽 탐색 )
                    start = mid+1
                    
            if find:
                break
                
                
        else:
            print('danger')

    except:
        break
        