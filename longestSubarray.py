class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        queue = []
        maxLen = -1
        maxx = []
        minn = []
        i = 0
        while i < len(nums) :
            while maxx and maxx[-1] < nums[i]:
                maxx.pop()
            maxx.append(nums[i])
            while minn and minn[-1] > nums[i] :
                minn.pop()
            minn.append(nums[i])
            queue.append(nums[i])  
            while maxx and minn and ((maxx[0] - minn[0]) > limit):                
                first = queue.pop(0)               
                if first == maxx[0]:
                    maxx.pop(0)
                if first  == minn[0]:
                    minn.pop(0)   
            maxLen = max(maxLen , len(queue))
            i += 1
        return maxLen 
