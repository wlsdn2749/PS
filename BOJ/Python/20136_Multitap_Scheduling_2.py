import heapq
import sys

SIZE = 500001
INF = 987654321

class Multi:
    def __init__(self, name, idx):
        self.name = name
        self.idx = idx

    def __lt__(self, other):
        return self.idx > other.idx

tap = []


def main():
    N, K = map(int, sys.stdin.readline().split())
    ans = 0
    cnt = 0
    
    q = [[] for _ in range(K+1)]
    arr = [0] * (K+1)
    visit = [0] * (K+1)
    
    temp = list(map(int, sys.stdin.readline().split()))
        
    for i in range(1, K+1):
        n = temp[i-1]
        arr[i] = n
        heapq.heappush(q[n], i)

    for i in range(1, K+1):
        if visit[arr[i]]: # 이미 멀티탭에 꽂혀 있는 경우에
            heapq.heappop(q[arr[i]]) # 다음 사용시점 제거
            if q[arr[i]]: # 다음 사용시점이 남아있다면
                heapq.heappush(tap, Multi(arr[i], q[arr[i]][0]))
            else:
                heapq.heappush(tap, Multi(arr[i], INF))
            continue

        if cnt < N: # 멀티탭에 자리가 남아있는 경우
            heapq.heappop(q[arr[i]]) # 다음 사용시점 제거 --> ok 합리적
            if q[arr[i]]: # 다음 사용 시점이 있다면
                heapq.heappush(tap, Multi(arr[i], q[arr[i]][0])) # (전기용품 번호, 다음 사용시점) push 
            else:
                heapq.heappush(tap, Multi(arr[i], INF))
            cnt += 1
            visit[arr[i]] = 1
        else:
            prev = heapq.heappop(tap) # 가장 나중에 나오는 거 미리 제거
            visit[prev.name] = 0 # 미리제거한거 visit 배열도 0으로 만들고
            heapq.heappop(q[arr[i]]) # 다음 사용시점 제거
            if q[arr[i]]: # 다음 사용시점이 있으면 넣어주고
                heapq.heappush(tap, Multi(arr[i], q[arr[i]][0]))
            else:
                heapq.heappush(tap, Multi(arr[i], INF))
            visit[arr[i]] = 1
            ans += 1 # 교환 여부

    print(ans)

if __name__ == "__main__":
    main()