from collections import defaultdict
N = int(input())

arr = sorted(list(map(int, input().split())))

# brute-force
added_dict = defaultdict(list) # append를 할때 key값 비어있을떄 valueError 대신 기본으로 [] 를 value로 넣어준 후 연산

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        added_dict[arr[i]+arr[j]].append((i, j)) # arr[i]+arr[j]를 key로, index pair를 value로 넣음 
        
cnt = 0
for idx in range(len(arr)): # 모든 정렬된 arr에 대해서
    for i, j in added_dict[arr[idx]]: # arr[idx]을 key로, 모든 value들을 돌아서
        if idx == i or idx == j: # 같은 idx라면, 자기 자신을 사용해서 값을 만든것이다. (0이 포함되있는 경우)
            continue
        else: # 아니라면 다른 2개를 합해서 구한 것
            cnt+=1
            break

print(cnt)