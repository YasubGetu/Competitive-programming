# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        half = []
        node = head
        
        while node:
            half.append(node.val)
            node = node.next
            
        start , end , count = 0 , len(half) - 1 , 0  
            
        while start < len(half):
            if start >= end:
                break
            start += 1
            end -= 1
       
        while head:
            if count == start:
                return head
            head = head.next
            count += 1
