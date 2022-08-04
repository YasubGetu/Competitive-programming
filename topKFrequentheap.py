class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict (int)
        answer = [] 
        mostFreq = set()
        
        for num in nums:
            count[num] -= 1
            
        freq = list(count.values()) 
        heapq.heapify(freq)
        
        i = 0
        while k > 0:
            if not mostFreq or freq[0] != a:
                a = heapq.heappop(freq)
                mostFreq.add(a)
            else:
                heapq.heappop(freq)
            k -= 1
            
        for key,val in count.items():
            if val in mostFreq:
                answer.append(key)
                
        return answer 
