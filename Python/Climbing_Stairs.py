class Solution(object):
    def climbStairs(self, n):
      if n == 1 or n == 2:
        return n
        
        prevPrev = 1
        prev = 2
        curr = 0

        for step in range(3, n + 1):
            curr = prevPrev + prev
            prevPrev = prev
            prev = curr
        return curr
