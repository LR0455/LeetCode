from collections import Counter
import os
from typing import Optional
from typing import List
os.chdir(os.path.dirname(__file__))

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= n-1
        return count
        

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    output = open(r'output', 'w')
    
    for i in range(len(input)):
        n = eval(input[i])
        sol = Solution()
        output.write(str(sol.hammingWeight(n)) + '\n')
    output.close()
    
if __name__ == "__main__":
    main()
