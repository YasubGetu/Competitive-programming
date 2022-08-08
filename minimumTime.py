class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        start , end = 1 , (min(time) * totalTrips) 
        ans = end
        while start <= end:
            mid = start + (end - start)//2
            total = 0
            for nums in time:
                total += (mid//nums)
                
            if total < totalTrips:
                start = mid + 1

            if total >= totalTrips:
                end = mid - 1
                ans = min(ans , mid)
                
        return ans        
            
