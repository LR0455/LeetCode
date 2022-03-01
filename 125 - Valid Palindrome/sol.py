from collections import Counter
import os
from typing import Optional
from typing import List
import re
os.chdir(os.path.dirname(__file__))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        i, j = 0, len(s)-1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    output = open(r'output', 'w')
    
    for i in range(len(input)):
        s = eval(input[i])
        sol = Solution()
        output.write(str(sol.isPalindrome(s)) + '\n')
    output.close()
    
if __name__ == "__main__":
    main()
