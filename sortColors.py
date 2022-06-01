class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        changer = 0
        for i in range(len(nums) ):
            for j in range(len(nums)):
                if nums[i] < nums[j]:
                    changer = nums[i]
                    nums[i] = nums [j]
                    nums[j] = changer
        
