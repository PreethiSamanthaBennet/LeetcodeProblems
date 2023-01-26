class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_indexes = []
        
        for i, s_c in enumerate(s):
            if s_c == c:
                c_indexes.append(i)
                
        result = []    
        
        for i, s_c in enumerate(s):
            min_distance = sys.maxsize
            for c_i in c_indexes:
                min_distance = min(abs(i - c_i), min_distance)
                                
            result.append(min_distance)
                   
        return result
