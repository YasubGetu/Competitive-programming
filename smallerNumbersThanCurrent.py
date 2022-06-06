class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dict = {}
        answer = []
        arrange = sorted(nums)
        for i in range(len(nums)):
            if arrange[i] not in dict:
                dict[arrange[i]] = i
        for i in range(len(nums)):  
             answer.append(dict [nums[i]])   
        return answer   
