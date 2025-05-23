from collections import defaultdict, deque
import sys

def solution(N, Q, edges, queries):
    # 그래프 생성
    graph = defaultdict(list)
    for p, q, r in edges:
        graph[p].append((q, r))
        graph[q].append((p, r))
    
    def dfs(v, k):
        visited = set()
        visited.add(v)
        st = deque([v])
        
        count=0 
        while st:
            cur = st.pop()
            for node, usado in graph[cur]:
                if node not in visited and usado >= k:
                    st.append(node)
                    visited.add(node)
                    count+=1
                    
        return count
        
        
    for k, v in queries:
        print(dfs(v, k))
        
        
if __name__ == "__main__":
    N, Q = map(int, input().split())
    
    edges = [] 
    for _ in range(N-1):
        p, q, r = map(int, input().split())
        edges.append((p, q, r))
        
    queries = []
    for _ in range(Q):
        k, v = map(int, input().split())
        queries.append((k, v))
        
    solution(N,Q,edges,queries)
        