import heapq
import sys

input = sys.stdin.readline

def dijkstra(start: int):
    
    pq = []
    INF = 100_000_000
    heapq.heappush(pq, (0, start)) # value , node
    distance_lst = [INF] * (n+1)
    
    distance_lst[start] = 0
    
    while pq:
        value, node = heapq.heappop(pq)
        
        for near_node, cost in arr[node]: # 인접노드에 대해서 search
            if distance_lst[near_node] > value + cost: 
                distance_lst[near_node] = value + cost # 최단거리갱신
                heapq.heappush(pq, (value+cost, near_node))
                
    
    return distance_lst
            
    
    


if __name__ == "__main__":
    T = int(input())
    
    for test_case in range(T):
        
        n, m, t = map(int, input().split())
        s, g, h = map(int, input().split())
        
        middle_cost = 0
        
        arr = [[] for _ in range(n+1)] # init
        dest = []
        for i in range(m):
            a, b, d = map(int, input().split())
            arr[a].append((b, d))
            arr[b].append((a, d)) # 양방향 연결선
            
            if a == g and b == h or a == h and b == g:
                middle_cost = d
                
        
        for i in range(t):
            dest.append(int(input()))
            
        # 다익스트라 (2->1, 3) and (1 -> 5,6 ... and 3 -> 5,6..)
        distance_lst = dijkstra(s) # 출발지에서 검색

        fst_cost = distance_lst[g] # 2 -> 1
        sec_cost = distance_lst[h] # 2 -> 3
        
        distance_lst_fst = dijkstra(h) # 3 -> 5,6..
        distance_lst_sec = dijkstra(g) # 1 -> 5,6..
        
        dest.sort()
        
        result = []
        for d in dest:
            fst = fst_cost + middle_cost + distance_lst_fst[d]
            sec = sec_cost + middle_cost + distance_lst_sec[d] 
            
            print("fst", fst, "sec", sec, "d",d)
            if distance_lst[d] == min(fst, sec):
                result.append(d)
                
        print(*result)
                
                
            
        
        
        
        
        
            
        
        
        
        