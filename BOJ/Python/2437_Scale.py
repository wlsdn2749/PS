N = int(input())

arr = sorted(list(map(int, input().split())))

dict = {}

if arr[0] != 1: # 첫번째 1이아니면 무조건
    print(1)
    exit(0)
    
else:   
    dp = [] 
    for i in range(len(arr)):
        # print(dp)
        if not dp:
            dp.append(arr[i])
            continue
        
        if dp:
            if dp[-1]+1 == arr[i]: # 가장 마지막 dp보다 arr[i]가 정확히 1 클 경우에 먼저 넣어주고 dp[-1]까지 반복
                prev_dp_len = len(dp)
                dp.append(arr[i])
                
                for j in range(prev_dp_len):
                    dp.append(arr[i]+dp[j])
                    dict[arr[i]+dp[j]] = 1
                    
            elif arr[i] in dp: # 이미 dp에 arr[i]가 있는경우
                prev_dp_len = len(dp)
                for j in range(prev_dp_len):
                    if not dict.__contains__(arr[i]+dp[j]):
                        dp.append(arr[i]+dp[j])
                        dict[arr[i]+dp[j]] = 1
                        
            else:
                print(dp[-1]+1)
                exit(0)
                
                
    print(sum(arr)+1)
                
                
                
                
                
             
            
        
        