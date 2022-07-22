class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        palindrome = []
        while head:
            palindrome.append(head.val)
            head = head.next 
        if palindrome == palindrome[::-1]:
            return True
        else:
            return False
