class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr_sum = 0
        ans = []
        
        for num in nums:
            curr_sum += num
            ans.append(curr_sum)
            
        return ans
