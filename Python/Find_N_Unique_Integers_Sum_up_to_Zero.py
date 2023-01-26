class Solution(object):
    def sumZero(self, n):
        ans = [i for i in range(1, (n // 2) + 1)]
        ans += [-i for i in ans]

        return ans if (n % 2 == 0) else ans + [0]
