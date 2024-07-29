from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        lst = [[] for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]
        is_cycle = False
        top = []
        
        def dfs(e, pts, roots):
            # print(pts, roots)
            nonlocal is_cycle
            
            # if pts == e or e in roots: # cycle
            #     is_cycle = True
            #     return
            
            visited[e] = True
            roots.append(e)
            
            for neighbor in lst[e]:
                if neighbor == pts or neighbor in roots:
                    is_cycle = True
                    return 
                
                if not visited[neighbor]:
                    dfs(neighbor, e, roots)
                
            top.append(e)
            roots.pop(-1)
        
        for a, b in prerequisites:
            lst[b].append(a)
            
        for a, b in prerequisites:
            
            if not visited[b]: 
                dfs(b, None, [])
            
            if is_cycle:
                return []
        
        for idx in range(numCourses):
            if idx not in top:
                top.append(idx)
                
        return list(reversed(top))
                
s = Solution()
print(s.findOrder(2, [[0,1]]))
print(s.findOrder(2, [[1,0]]))
print(s.findOrder(2, [[0,1], [1,0]]))
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(s.findOrder(3, [[2,0],[2,1]]))
print(s.findOrder(3, [[1,0],[0,2],[2,1]]))
print(s.findOrder(1, []))
    
            
        
        