class Solution: 
    def select(self, arr, i):
        for j in range(len(arr)):
           if arr[j] > i:
               arr[j] , i = i , arr[j]
        return arr       
    def selectionSort(self, arr,n):
        arr.sort()
