class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        maxx = (2 ** p) - 1
        return (pow((maxx - 1) , ((maxx - 1)//2) , 1000000007) * maxx ) % (1000000007)    
