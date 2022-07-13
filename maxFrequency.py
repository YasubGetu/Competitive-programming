class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        r , l , tot , res = 0 , 0 , 0 , 0
        
        nums.sort()
        
        while r < len(nums):
            tot += nums[r]
            
            while (nums[r] * (r - l + 1)) > tot + k:
                tot -= nums[l]
                l += 1
                
            res = max(res , r - l + 1)    
            r += 1
            
        return res            
            
