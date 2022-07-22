class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        node = head
        answer , res , stack = [] , [] , []
        
        while node:
            answer.append(node.val)
            node = node.next
            
        res = answer[:]
        
        for i , num in enumerate (res):
            
            while stack and answer[stack[-1]] < num:
                prevIndex = stack.pop()
                answer[prevIndex] = num
                
            stack.append(i)  
            
        for i in range (len(answer)):
            
            if answer[i] == res[i]:
                answer[i] = 0
                
        return answer        
