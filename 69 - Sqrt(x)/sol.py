from collections import Counter
import os
from typing import Optional
from typing import List
os.chdir(os.path.dirname(__file__))

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    output = open(r'output', 'w')
    
    for i in range(len(input)):
        x = eval(input[i])
        sol = Solution()
        output.write(str(sol.mySqrt(x)) + '\n')
    output.close()
    
if __name__ == "__main__":
    main()
