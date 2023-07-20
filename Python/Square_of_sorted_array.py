import numpy

class Solution(object):
    def sortedSquares(self, nums):
        squared = numpy.square(nums)
        return sorted(squared)
        
        
