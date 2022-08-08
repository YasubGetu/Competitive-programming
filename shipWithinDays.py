class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        start , end = max(weights) , sum(weights)
        ans , count , summ = end , 0 , 0
        n = len(weights)
        
        while start <= end:
            
            mid = start + (end - start)//2
            
            for i in range (len(weights)):
                summ += weights[i]
                
                if summ > mid:
                    count += 1
                    summ = weights[i]
 
                if i == n - 1:    
                    if count + 1 <= days:
                        end = mid - 1
                        ans = min(ans , mid)
                    else:
                        start = mid + 1
                        
                elif count > days:
                    start = mid + 1
                    break
                    
            summ = count = 0
            
        return ans    
                                             
