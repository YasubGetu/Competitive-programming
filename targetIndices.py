class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        collect = []
        nums.sort()
        for i in range (len(nums)):
            if nums[i] == target:
                collect.append(i)
                if nums[i] != nums[-1] and nums[i] != nums[i+1]:
                    break
        return collect            
             
