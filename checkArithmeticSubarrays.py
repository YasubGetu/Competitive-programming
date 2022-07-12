class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        is_arit = []
        
        for i in range (len(l)):
            arr = nums[l[i]:r[i] + 1]
            arr.sort()
            x = 1   
            
            for j in range (len(arr) - 1):
                if arr[j + 1] - arr[j] != arr[1] - arr[0]:
                    is_arit.append(False)
                    break
                else:
                    x += 1
                    if x == len(arr):
                        is_arit.append(True)
                        
        return is_arit                    
