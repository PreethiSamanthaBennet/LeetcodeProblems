class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return -1
        nums.sort()
        return nums[1]
