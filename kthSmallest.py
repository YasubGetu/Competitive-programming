class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        sorter = []
        for i in matrix:
            sorter.extend(i)
            
        heapq.heapify(sorter)

        for i in range(1 , k):
            heapq.heappop(sorter)
        return sorter[0]
        

