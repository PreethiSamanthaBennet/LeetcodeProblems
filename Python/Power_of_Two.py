class Solution(object):
    def isPowerOfTwo(self, n):
        if(n <= 0):
            return False
        while(n % 2 == 0):
            n = n/2
        return n == 1
