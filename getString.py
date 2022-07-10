class Solution:
    def getString(self, n: int, k: int) -> str:
        def invert(arr):
            return "".join("0" if i == "1" else "1" for i in arr)
          
        if n == 1:
            return "0"
          
        arr = self.getString(n - 1 , k)
        string = arr + "1" + invert(arr)[::-1]
        return string
      
    def findKthBit(self, n: int, k: int) -> str:
        return self.getString(n , k)[k - 1]
