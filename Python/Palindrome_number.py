class Solution(object):
    def isPalindrome(self, x):
        reverse = 0
        tempOriginal = x

        while tempOriginal > 0:
            lastDigit = tempOriginal % 10
            reverse = reverse * 10 +lastDigit 
            tempOriginal = tempOriginal / 10

        if x == reverse:
            return True

        else:
            return False
