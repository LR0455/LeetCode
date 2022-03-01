from collections import Counter
import os
from typing import Optional
from typing import List
os.chdir(os.path.dirname(__file__))

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        for i in range(1, rowIndex+1):
            res.append([1 for _ in range(i+1)])
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res[rowIndex]

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    output = open(r'output', 'w')
    
    for i in range(len(input)):
        rowIndex = eval(input[i])
        sol = Solution()
        output.write(str(sol.getRow(rowIndex)) + '\n')
    output.close()
    
if __name__ == "__main__":
    main()
