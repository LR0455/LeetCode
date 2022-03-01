from collections import Counter
import os
from typing import Optional
from typing import List
os.chdir(os.path.dirname(__file__))

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    output = open(r'output', 'w')
    
    for i in range(len(input)):
        s = eval(input[i])
    
        sol = Solution()
        output.write(str(sol.lengthOfLastWord(s)))
    output.close()
    
if __name__ == "__main__":
    main()
