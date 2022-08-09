class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start , end =  0 , len(matrix) - 1
        while start <= end:
            mid = start + (end - start)//2
            if matrix[mid][0] > target:
                end = mid - 1
            elif matrix[mid][-1] < target:
                start = mid + 1
            elif matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            elif matrix[mid][0] < target and matrix[mid][-1] > target:
                left , right = 1 , len(matrix[mid]) - 1
                while left <= right:
                    middle = left + (right - left)//2
                    if matrix[mid][middle] == target:
                        return True
                    if matrix[mid][middle] > target:
                        right = middle - 1
                    elif matrix[mid][middle] < target:
                        left = middle + 1
                        
                return False
            
        return False
