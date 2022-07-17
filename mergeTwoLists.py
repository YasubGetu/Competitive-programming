# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        order = []
        
        while node1 and node2:
            order.append(node1.val)
            order.append (node2.val)
            node1 = node1.next
            node2 = node2.next
            
        while node1 and not node2:
            order.append(node1.val)
            node1 = node1.next
            
        while node2 and not node1:
            order.append (node2.val)
            node2 = node2.next
            
        order.sort() 
        
        if len(order):
            merged = ListNode(order[0])
            mergedHead = merged
        else:
            return node1
        
        for i in range (1,len(order)):
            mergedNodes = ListNode(order[i])
            merged.next = mergedNodes
            merged = merged.next
            
        return mergedHead    
             
