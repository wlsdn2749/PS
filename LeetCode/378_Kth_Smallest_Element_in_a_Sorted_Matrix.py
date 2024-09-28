import heapq

class Solution:
    def kthSmallest(self, matrix, k) -> int:
        
        # 1st solution, O(n^2) Memory Complexity
        
        '''
        flatten_lst = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                flatten_lst.append(matrix[i][j])
                
        flatten_lst.sort()
        return flatten_lst[k-1]
        '''
        
        # 2nd solution, O(1) Memory Complexity, Max Heap
        '''
        max_heap = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                heapq.heappush(max_heap, -matrix[row][col])
                if len(max_heap) > k:
                    heapq.heappop(max_heap)
                    
        return -heapq.heappop(max_heap)
        '''
        # 3rd solution, O(1) Memory Complexity, Min Heap
        pass
    
        # 4rd solution O(1) Memory Complexity and O(n) Time Complexity Binary Search
        def count_less_equal(x):
            c = len(matrix[0]) - 1
            
            count = 0
            for r in range(len(matrix)):
                
                while c >= 0 and matrix[r][c] > x:
                    c -= 1
                    
                count += c + 1
            
            return count
        
    
        left, right = matrix[0][0], matrix[-1][-1]
        
        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) < k:
                left = mid + 1
            
            else:
                right = mid
        
        return left
                        
        
s = Solution()
print(s.kthSmallest(matrix=[[1,5,9],[10,11,13],[12,13,15]], k=8))