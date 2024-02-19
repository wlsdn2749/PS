import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int ,input().split())

# 친구관계 네트워크 
network = [[] for i in range(N)] 
num_list = [0] * 2000
visited = [0] * 2000
def dfs(index, arr):    
    # print(arr)
  
    if len(arr) == 5:
        print(1)
        exit(0)
        
    for node in network[index]:
        if not visited[node]:
            arr.appendleft(node)
            visited[node] = 1
            dfs(node, arr)
            
            visited[node] = 0
            arr.popleft()
    
    
# 구축
for i in range(M):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)
    
# 친구관계 네트워크 DFS + BT

for i in range(N):
    num_list = [0] * 2000
    visited = [0] * 2000
    arr = deque()
    arr.appendleft(i)
    visited[i] = 1
    dfs(i, arr)
    
print(0)

