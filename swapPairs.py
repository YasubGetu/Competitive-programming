class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0 , head)
        prev , curr = dummy , head
        
        while curr and curr.next:
            nextPair = curr.next.next
            second = curr.next
            
            prev.next = second
            second.next = curr
            curr.next = nextPair
            
            prev = curr
            curr = nextPair
        return dummy.next
        
