class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sets = set(wordDict)
        
        @functools.lru_cache(None)
        def wordBreak(s: str) -> bool:
            if s in sets:
                return True
            return any(s[:i] in sets and wordBreak(s[i:]) for i in range(len(s)))
        return wordBreak(s)
