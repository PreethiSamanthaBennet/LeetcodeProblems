class Solution:
    def isGood(self, nums: List[int]) -> bool:
        N = len(nums)
        c = collections.Counter(nums)

        for i in range(1, N - 1):
            if c[i] != 1:
                return False

        return c[N - 1] == 2
