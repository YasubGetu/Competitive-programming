class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:       
        original = []
        count = defaultdict(int)
        changed.sort()
        for num in changed :
            count[num] += 1
        for i in range(len(changed)):
            if count[changed[i]] !=0 and count[2 * changed[i]] != 0:
                count [changed[i]] -= 1
                count[2 * changed[i]] -= 1
                original.append(changed[i])
            elif count [changed[i]] != 0 and count[2*changed[i]] == 0:
                return []
        if len(original) != int(len(changed)/2):
            return []
        else:
            return original       
    
    
    
    
           
