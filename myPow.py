class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n == 1.0:
            return x
        if n % 2 == 0:
            power = self.myPow(x, n/2)
            return power * power
        else:
            if n > 0:
                power = self.myPow(x, n//2)
                return power * power * x
            else:
                power = self.myPow(x, - (abs(n) // 2)) 
                return power * power * 1/x
