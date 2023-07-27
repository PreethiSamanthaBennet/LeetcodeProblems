class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)

        left = 1
        right =sum(batteries)//n

        def good(target):
            contribution = 0
            for b in batteries:
                contribution += min(target, b)

            return contribution >= (n*target)

        while left < right:
            mid = (left+right+1)//2

            if good(mid):
                left = mid

            else:
                right = mid - 1

        return left
