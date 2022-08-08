class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        start , end = 1 , n
 
        while start <= end:
            mid = start + (end - start)//2
            it_self , count = 0 , 0
            for i in range (len(nums)):
                if nums[i] >= mid:
                    count += 1
                if nums[i] == mid:
                    it_self += 1
                  
            if count > n+1 - mid:
                if it_self > 1:
                    return mid
                else:
                    start = mid + 1
            else:
                end = mid - 1
