from collections import Counter
import os
from typing import Optional
from typing import List
os.chdir(os.path.dirname(__file__))

class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [0 for _ in range(50)]
        fib[0] = 1
        fib[1] = 1
        for i in range(2, n+1):
            fib[i] = fib[i-2] + fib[i-1]
        
        return fib[n]
        

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    output = open(r'output', 'w')
    
    for i in range(len(input)):
        n = eval(input[i])
        sol = Solution()
        output.write(str(sol.climbStairs(n)) + '\n')
    output.close()
    
if __name__ == "__main__":
    main()
