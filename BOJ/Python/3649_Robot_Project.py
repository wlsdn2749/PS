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

        # 투 포인터

        first = 0
        end = N-1

        while first < end:
            # print(first, end)

            diff = arr[end] + arr[first] 
            
            if x == diff: # 만약 구멍을 완전히 틀어막을 수 이쓰면?
                print(f'yes {arr[first]} {arr[end]}')
                break

            elif x > diff: # 너비 보다 두 볼트의 합이 작을 경우 first를 오른쪽으로
                first += 1
                
            else: # 너비 보다 두 볼트의 합이 클 경우 end를 왼쪽으로
                end -= 1           
            
        else:
            print('danger')

    except:
        break
        