class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res, n = 0, len(nums)

        for i, v in enumerate(nums, 1):
            if n % i == 0:
                res += v**2

        return res
