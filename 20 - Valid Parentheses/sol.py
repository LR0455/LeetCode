from collections import Counter
import os
from typing import List
os.chdir(os.path.dirname(__file__))

class Solution:
    def isPair(self, left: chr, right: chr):
        if left + right in ['()', '{}', '[]']:
            return True
        return False
    def isValid(self, s: str) -> bool:
        stk = []
        
        for c in s:
            if c in ['(', '{', '[']:
                stk.append(c)
            elif not stk:
                return False
            else:
                if self.isPair(stk[-1], c):
                    stk.pop()
                else:
                    return False
        
        return False if stk else True

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    
    s = eval(input[0])
    
    output = open(r'output', 'w')
    sol = Solution()
    output.write(str(sol.isValid(s)))
    output.close()
    
if __name__ == "__main__":
    main()
