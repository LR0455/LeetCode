from collections import Counter
import os
from typing import Optional
from typing import List
os.chdir(os.path.dirname(__file__))

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(t) != len(s) or len(set(s)) != len(set(t)):
            return False
        
        mapping = dict()
        for i in range(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = t[i]
            elif mapping[s[i]] != t[i]:
                return False
                            
        return True

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    output = open(r'output', 'w')
    
    for i in range(0, len(input), 2):
        s = eval(input[i])
        t = eval(input[i+1])
        sol = Solution()
        output.write(str(sol.isIsomorphic(s, t)) + '\n')
    output.close()
    
if __name__ == "__main__":
    main()
