# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
         
        node1 = l1
        node2 = l2
        len1 , len2 = 0 , 0
        num1 , num2 = "" , ""
        
        while node1:
            num1 = str(node1.val) + num1
            node1 = node1.next
            len1 += 1
            
        while node2:
            num2 = str(node2.val) + num2
            node2 = node2.next
            len2 += 1
            
        length = max(len1 , len2)
        sums = (int(num1) + int(num2))
        sums = str(sums)
        newHead = None
        i = 0
        
        while i < len(sums):
            newNode = ListNode(sums[i])
            newNode.next = newHead
            newHead = newNode
            i += 1
            
        return newHead     
