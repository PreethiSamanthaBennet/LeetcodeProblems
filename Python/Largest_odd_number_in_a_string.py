class Solution:
    def largestOddNumber(self, num: str) -> str:
        N = len(num)

        index = N - 1

        while index >= 0 and int(num[index])%2 == 0:
            index -= 1

        if index < 0:
            return ""
        return num[:index+1]
