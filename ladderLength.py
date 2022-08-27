class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        related = collections.defaultdict(list)
        visited = set([beginWord])
        wordList.append(beginWord)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1 : ]
                related[pattern].append(word)
        res = 1        
        q = deque([beginWord])        
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1 :]
                    for relatedWord in related[pattern]:
                        if relatedWord not in visited:
                            q.append(relatedWord)
                            visited.add(relatedWord)
                        
            res += 1 
        return 0    
