class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        count = 0
        i = 0
        
        while count < len(nums):   
        
            if nums[i] == 0:
            
                nums.pop(i)
                nums.append(0)
                i -= 1
                
            count += 1
            i += 1
