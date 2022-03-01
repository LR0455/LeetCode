from collections import Counter
import os
from typing import Optional
from typing import List
os.chdir(os.path.dirname(__file__))

class Solution:
    def isHappy(self, n: int) -> bool:
        exist = dict()
        while n != 1:
            tmp = 0
            while n:
                tmp += (n%10) ** 2
                n //= 10
            if tmp in exist:
                return False
            exist[tmp] = True
            n = tmp
        return True

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    output = open(r'output', 'w')
    
    for i in range(len(input)):
        n = eval(input[i])
        sol = Solution()
        output.write(str(sol.isHappy(n)) + '\n')
    output.close()
    
if __name__ == "__main__":
    main()
