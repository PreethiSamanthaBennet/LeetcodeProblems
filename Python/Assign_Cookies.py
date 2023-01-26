class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result, i = 0, 0
        for j in range(len(s)):
            if i == len(g):
                break
            if s[j] >= g[i]:
                result += 1
                i += 1
        return result
