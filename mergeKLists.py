class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ac = []
            
        for i in lists:
            while i:
                ac.append(i.val)
                i = i.next
                
        ac.sort()
        newList = top = ListNode()
        
        for i in ac:
            newList.next = ListNode(i)
            newList = newList.next
         
        return top.next
