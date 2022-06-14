class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = int(len(nums)/2)
        nums.sort()
        pairs = nums[: n].copy()
        x = 0
        for i in range(n):
            pairs[i] = (nums[x] , nums[ -x - 1])
            x += 1   
            nums[i] = pairs[i][0] + pairs[i][1] 
        return max(nums)
            
