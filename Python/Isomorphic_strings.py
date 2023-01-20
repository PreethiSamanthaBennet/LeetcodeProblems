class Solution(object):
    def isIsomorphic(self, s, t):
        letterMap = {}
        reverseMap = {}

        for i in range(len(s)):
            letter_s = s[i]
            letter_t = t[i]

            if letter_s in letterMap and letterMap[letter_s] != letter_t:
                return False

            if letter_t in reverseMap and reverseMap[letter_t] != letter_s:
                return False

            letterMap[letter_s] = letter_t
            reverseMap[letter_t] = letter_s

        return True
