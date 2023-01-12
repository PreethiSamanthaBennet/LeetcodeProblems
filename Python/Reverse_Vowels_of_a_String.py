class Solution:
    def reverseVowels(self, s: str) -> str:
        charList = list(s)
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l = 0
        r = len(s) - 1
        
        while l < r:
            while l < r and charList[l] not in vowel:
                l += 1
            while l < r and charList[r] not in vowel:
                r -= 1
            charList[l], charList[r] = charList[r], charList[l]
            l += 1
            r -= 1
        return ''.join(charList)
