from collections import Counter
import os
from typing import Optional
from typing import List
os.chdir(os.path.dirname(__file__))

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        count = 0
        while count < 32:
            res = res * 2 + n%2
            n //= 2
            count += 1
            
        return res
        

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    output = open(r'output', 'w')
    
    for i in range(len(input)):
        n = eval(input[i])
        sol = Solution()
        output.write(str(sol.reverseBits(n)) + '\n')
    output.close()
    
if __name__ == "__main__":
    main()
