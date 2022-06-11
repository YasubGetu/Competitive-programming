class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        for i in range (len(nums)):
            half = k - nums[i]
            if count[nums[i]] != 0 and count[half] != 0 and nums[i] != half:
                count[nums[i]] -= 1
                count[half] -= 1
                operations += 1
            if nums[i] == half:
                if count[nums[i]] >1:
                    count[nums[i]] -= 1
                    count[half] -= 1
                    operations += 1                 
        return operations
