class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0, 0
        RS, LS = [0], [0]
        
        for i in range(len(nums) - 1):
            rightSum += nums[i]            
            RS.append(rightSum)
            leftSum += nums[-i - 1]
            LS.append(leftSum)
            
        LS = LS[::-1]

        for i in range(len(nums)):
            if LS[i] == RS[i]:
                return i
            
        return -1
