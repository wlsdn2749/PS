'''
    트리의 지름은
    임의의 한 노드에서 DFS한 후,
    
    DFS가 끝난 노드에서 다시한번 DFS하고 최대 값을 구하면 된다.
'''

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

cur_max = 0
max_node = -1

def dfs(root, prev_root, distance):
    global max_node, cur_max
    
    for node, cost in graph[root]:
        
        if node != prev_root:
            dfs(node, root, distance+cost)
            
    if cur_max < distance:
        max_node = root
        cur_max = distance
        
        
n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    
    graph[a].append((b,c))
    graph[b].append((a,c))


dfs(1, -1, 0)
dfs(max_node, -1, 0)

print(cur_max)

    