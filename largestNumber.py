class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        changer = []
        for i in range(len(nums)):
            changer.append(str(nums[i]))
        def compare (n1 , n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        changer = sorted(changer , key = cmp_to_key(compare))    
        return str(int("".join(changer)))
