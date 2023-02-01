class Solution(object):
    def addBinary(self, a, b):
        
        result = ""
        aCt = len(a) - 1
        bCt = len(b) - 1

        carry = 0

        while aCt >= 0 or bCt >= 0:
        
            totalSum = carry
            if aCt >= 0:
                totalSum += int(a[aCt])
                aCt -= 1
            if bCt >= 0:
                totalSum += int(b[bCt])
                bCt -= 1
                
            # Add the bit to the result
            result = str(totalSum % 2) + result
            
            # Modify the carry
            carry = totalSum // 2
            
        # Final check if carry exists
        if carry > 0:
            result = str(1) + result
        return result
