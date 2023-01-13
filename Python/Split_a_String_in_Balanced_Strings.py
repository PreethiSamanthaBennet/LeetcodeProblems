class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = l = 0
        for c in s:
            if c == 'L':
                l += 1
            else:
                l -= 1
            if l == 0:
                result += 1
        return result
