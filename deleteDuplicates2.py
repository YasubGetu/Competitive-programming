class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head
        count = defaultdict (int)
        
        if not head:
            return head
        
        while node:
            count[node.val] += 1
            node = node.next
            
        node = head
        
        while node and count[node.val] > 1:
            head = node.next
            node = node.next
        
        while node and node.next:
            if count[node.next.val] > 1:
                node.next = node.next.next
            else:    
                node = node.next
                
        return head     
