class Solution:    
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        start , end = 1 , m*n
        while start <= end:
            count , temp = 0 , 0
            mid = start + (end - start)//2
                             
            if start == end:
                return start
            for i in range(1 , m+1):
                temp = min(mid//i , n)
                count += temp
   
            if count >= k :
                end = mid
            elif count < k:
                start = mid + 1
