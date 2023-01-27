class Solution(object):
    def generate(self, numRows):
        rowArray = []

        for i in range(numRows):
            rowArray.append([])
            
            for j in range(i + 1):
                if j == 0 or j == i:
                    rowArray[i].append(1)
                else:
                    rowArray[i].append(rowArray[i - 1][j - 1] + rowArray[i - 1][j])
        return rowArray        
