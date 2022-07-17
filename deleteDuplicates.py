# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        node = head
        
        while node:
            nums.append(node.val)
            node = node.next
        if not head:
            return head
        
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        
        newHead = ListNode(nums[0])
        theHead = newHead
        
        for i in range (1 , len(nums)) :
            newNode = ListNode(nums[i])
            newHead.next = newNode
            newHead = newHead.next
        
        return theHead
    
        """ OR
        node = head
        
        if not head:
            return head
            
        while node.next:
        
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
                
        return head    """
        
        
        
