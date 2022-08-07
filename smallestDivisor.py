class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start , end = 1 , max(nums) 
        divisor =1000000
        
        while start <= end:
            mid = start + (end - start)//2
            div = []
            
            for num in nums:
                if num%mid == 0:
                    val = num/mid
                else:
                    val = num//mid + 1
                div.append(val) 
                
            total = sum(div)
            if total <= threshold and divisor > mid:
                end = mid - 1
                divisor = mid
            if total > threshold:        
                start = mid + 1
                
        return divisor 
