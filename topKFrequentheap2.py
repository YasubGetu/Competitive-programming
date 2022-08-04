class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = defaultdict (int)
        answer , ans = [] , []
        
        for word in words:
            count[word] -= 1
            
        for i in count:
            answer.append([count[i] , i])
            
        heapq.heapify(answer)  
        
        for i in range (k):
            ans.append(heapq.heappop(answer)[1])
        return ans        
