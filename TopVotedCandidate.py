class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.maximum = []
        self.count = defaultdict (int)
        
        for i in range(len(self.persons)):
            self.count[persons[i]] += 1
            self.reverseIt = persons[:i + 1]
            self.reverseIt.reverse()
            self.maxx = max(self.count.values())
            i = 0
            while i < len(self.reverseIt):
                if self.maxx == self.count[self.reverseIt[i]]:
                    self.maximum.append(self.reverseIt[i])
                    break
                i += 1                
            
    def q(self, t: int) -> int:
        
        start , end , q = -1 , len(self.times) - 1 , 0
        sorter = []
                
        while start <= end:
            mid = start + (end - start)//2
            
            if self.times[mid] > t:
                end = mid - 1
            elif self.times[mid] < t:
                start = mid + 1
                q = max(mid , q)                

            elif self.times[mid] == t:
                q = mid
                break
                
        if q == 0:
            return self.persons[0]
               
        return self.maximum[q]         
            

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
