class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            if n %3 != 0: return False
            n /= 3
        return n == 1
