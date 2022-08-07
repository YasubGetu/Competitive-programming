class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        start , end = 0 , n - 1
        
        while start <= end:
            mid = start + (end - start)//2            
            
            if isBadVersion(mid + 1):
                end = mid
            else:
                start = mid + 1
                
            if start == end:
                return start + 1    
                
        return mid + 1  
