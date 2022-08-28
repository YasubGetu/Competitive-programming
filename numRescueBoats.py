class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        start , end = 0 , len(people) - 1
        while start <= end:
            if start == end:
                count += 1
                return count
            if people[start] + people[end] <= limit:
                end -= 1
                start += 1
                count += 1
                
            else:
                end -= 1
                count += 1
        return count            
