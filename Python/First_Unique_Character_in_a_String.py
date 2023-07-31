class Solution:
    def firstUniqChar(self, s: str) -> int:
        st_map = {}

        for i in range(0, len(s)):
            if s[i] not in st_map:
                st_map[s[i]] = True

            else:
                st_map[s[i]] = False

        for i in range(0, len(s)):
            if st_map[s[i]]:
                return i
        return -1
