def has_cycle(head):
    
    node = head
    nextNode = head
    
    while nextNode and nextNode.next:
        
        node = node.next
        nextNode = nextNode.next.next 
        if node == nextNode:
            return 1
        
    return 0
