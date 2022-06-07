class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        check = []       
        for i in range(len(nums)):
            check.append(int(nums [i])) 
        check.sort()     
        for i in range(len(nums)):
            if (len(nums) - i) == k:
                return str(check[i])
