class Solution:
    def hIndex(self, citations: List[int]) -> int:
        start , end , h = 0 , len(citations) - 1 , 0
        
        while start <= end:
            
            mid = start + (end - start)//2
            length = len(citations) - mid
            
            if citations[mid] >= length and h < length:
                h = length
                end = mid - 1
            if citations[mid] < length:
                start = mid + 1
                           
        return h 
