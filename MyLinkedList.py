class ListNode:
    def __init__(self , val = 0 , next = None):
        
        self.val = val
        self.next = next
        
class MyLinkedList:
    def __init__ (self):
        self.size = 0
        self.head = ListNode()

    def get(self, index: int) -> int:
        
        if index >= self.size or index < 0:
            return -1
        
        current = self.head
        
        for _ in range(index + 1):
            current = current.next
            
        return current.val    

    def addAtHead(self, val: int) -> None:
        
        self.addAtIndex(0 , val)

    def addAtTail(self, val: int) -> None:
        
        self.addAtIndex(self.size , val)

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.size:
            return
        
        pre = self.head
        
        for _ in range(index):
            pre = pre.next
            
        insert = ListNode(val)
        insert.next = pre.next
        pre.next = insert
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        
        if index >= self.size or index < 0:
            return 
       
        pre = self.head
        
        for _ in range(index):
            pre = pre.next
            
        pre.next = pre.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
