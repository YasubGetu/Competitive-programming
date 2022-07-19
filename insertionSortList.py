# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        newNode = ListNode(head.val)
        newHead = newNode
        head = head.next
        
        while head: 
            
            if head.val >= newNode.val:
                newNode1 = ListNode(head.val)
                newNode.next =newNode1
                newNode = newNode.next
                head = head.next
                
            elif head.val < newNode.val:
                newPtr = newHead
                
                if head.val <= newPtr.val:
                    aNode = ListNode(head.val)
                    aNode.next = newHead
                    newHead = aNode
                    head = head.next
                    
                elif head.val > newPtr.val:
                    
                    curr = newPtr.next
                    
                    while curr and head:
                        
                        if head.val >= curr.val:
                            curr = curr.next
                            newPtr = newPtr.next
                            
                        else:
                            
                            insert = ListNode(head.val)
                            newPtr.next = insert
                            insert.next = curr
                            head = head.next
                            break
                            
        return newHead           
                        
                
        
        
        
        
        
        
        
