class Solution(object):
    def singleNumber(self, nums):
        hashTable = {}
        for i in nums:
            try:
                hashTable.pop(i)
            except:
                hashTable[i] = 1
        return hashTable.popitem()[0]
