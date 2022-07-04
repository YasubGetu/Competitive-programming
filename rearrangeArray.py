class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a = 0
        b = 0
        stack = []
        nums.sort()
        for i in range(len(nums)):
            if i % 2 == 0:
                stack.append(nums[a])
                a += 1
                    
            else:
                stack.append(nums[-(b + 1)])
                b += 1
        return stack       
