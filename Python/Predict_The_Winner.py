class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0 or len(nums) == 1:
            return True

        dp = [0] * len(nums)

        for i in reversed(range(len(nums))):
            dp[i] = nums[i]

            for j in range(i+1, len(nums)):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[-1] >= 0
