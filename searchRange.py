class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = self.binarysearch(nums , target , True)
        right = self.binarysearch(nums , target , False)
        return [left , right]
                
    def binarysearch(self , nums , target , leftbias):
        start , end = 0 , len(nums) - 1
        i = -1
        while start <= end:
            mid = end + (start - end)//2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                i = mid
                if leftbias:
                    end = mid - 1
                else:
                    start = mid + 1
        return i         
                
        
