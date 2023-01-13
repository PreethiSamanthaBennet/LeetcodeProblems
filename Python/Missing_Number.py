class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        visit = set()
        
        for num in nums:
            visit.add(num)
        
        for i in range(0, n + 1):
            if i not in visit:
                return i
