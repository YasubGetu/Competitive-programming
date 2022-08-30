class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        maxIndex = {}
        visited = set()
        ans = []
        for i in range(len(s)):
            maxIndex[s[i]] = i
        
        for i in range(len(s)):
            if s[i] in visited:
                continue
            while ans and ans[-1] > s[i] and maxIndex[ans[-1]] > i:
                visited.remove(ans[-1])
                ans.pop()
            visited.add(s[i])
            ans.append(s[i])
            
        return "".join(ans)
