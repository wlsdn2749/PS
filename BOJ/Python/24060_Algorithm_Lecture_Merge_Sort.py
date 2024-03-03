import sys
input = sys.stdin.readline

N, K = map(int, input().split())

A = list(map(int, input().split()))

cnt = 0
result = -1

def merge_sort(left, right):
    
    if left < right:
        
        mid = (left+right) // 2 
        
        merge_sort(left, mid)
        merge_sort(mid+1, right)
        merge(left, mid, right) # 병합
    

def merge(left, mid, right):
    global cnt, result
    i = left
    j = mid+1
    t = 0
    tmp = [0] * (right - left + 1)
    
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
            t += 1
        else:
            tmp[t] = A[j]
            j += 1
            t += 1
            

    
    while i <= mid: # 왼쪽 배열이 남은 경우
        tmp[t] = A[i]
        i += 1
        t += 1
    
    while j <= right: # 오른쪽 배열이 남은경우
        tmp[t] = A[j]
        j += 1
        t += 1
        
    i = left
    t = 0
    
    while i <= right:
        cnt += 1 
        if cnt == K:
            result = tmp[t]
            print(result)
            exit(0)
        A[i] = tmp[t]
        i += 1
        t += 1

merge_sort(0, N-1)
print(result)

