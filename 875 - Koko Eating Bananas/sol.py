from collections import Counter
import math
import os
from typing import List
os.chdir(os.path.dirname(__file__))
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, 1e9
        while (left < right):
            k = (left + right) // 2
            H = 0
            for p in piles:
                H += math.ceil(p / k)
            if H > h:
                left = k+1
            else:
                right = k
        
        return int(left)
def main():
    input = open(r'input', 'r')
    input = input.readlines()
    
    piles = eval(input[0])
    h = eval(input[1])
    
    output = open(r'output', 'w')
    sol = Solution()
    output.write(str(sol.minEatingSpeed(piles, h)))
    output.close()
    
if __name__ == "__main__":
    main()
