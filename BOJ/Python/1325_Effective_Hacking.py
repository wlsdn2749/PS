import sys
sys.setrecursionlimit(10**5)


def get_input():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)] # 0번 인덱스는 안씀
    
    for _ in range(M):
        a, b = map(int, input().split())
        graph[b].append(a)

    return N, M, graph

def search(a: int):
    depth = 1
    visited.add(a)
    
    # if count[a] != 0:
    for i in graph[a]:
        if i not in visited:
            if count[i] != 0:
                return depth + count[i]
            else:
                depth += search(i)
            
    count[a] = depth
    
    print(count)    
    return depth
    
def solution():
    global visited, max, targets, count
    
    for i in range(1, N+1):
        a = search(i)
        count[i] = a
        visited = set()
        if max < count[i]:
            max = a
            targets = []
        
        if max == count[i]:
            targets.append(i)
    
    for target in targets:
        print(target, end=" ")
        
if __name__ == "__main__":
    N, M, graph = get_input()
    visited = set()
    max = 0
    targets = []
    count = [0 for _ in range(N+1)]
    solution()
    