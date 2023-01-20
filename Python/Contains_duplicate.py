class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = set()
        
        for n in nums:
            if n not in counter:
                counter.add(n)
            else:
                return True
            
        return False
