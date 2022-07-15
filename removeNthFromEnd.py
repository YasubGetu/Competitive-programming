# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length , count = 0 , 2
        node = head
        
        while node:
            length += 1
            node = node.next

        prev = head
        curr = prev.next        
        delete = length - n + 1
        
        while curr:
            
            if delete == 1:
                head = head.next
                return head
            
            if count == delete:
                prev.next = curr.next
                return head
            
            count += 1
            curr = curr.next
            prev = prev.next
        
