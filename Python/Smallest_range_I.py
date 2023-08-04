class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()

        target = nums[0] + k 

        best = 0

        for num in nums:
            best = max(best, max(abs(num - target) - k, 0))
        return best
