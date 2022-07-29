class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
              
        longest , start , end = 0 , 0 , 1 
        
        if len(s) == 1:
            return 1
        
        while end < len(s):
            
            if s[end] in s[start : end]:
                start += 1
            else:
                end += 1
                   
            longest = max(end - start , longest)
            
        return longest 
