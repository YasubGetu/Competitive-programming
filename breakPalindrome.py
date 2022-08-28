class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        ans = ""
        if n == 1:
            return ""
        for letter in range(n):
            if palindrome[letter] == "a" and letter == n-1:
                ans = palindrome[:letter] + "b"
                return ans
            if palindrome[letter] == "a":
                continue
            else: 
                ans = palindrome[:letter] + "a" + palindrome [letter+1:] 
                if ans.count("a") == n:
                    return (palindrome[:-1] + "b")
                return ans  
