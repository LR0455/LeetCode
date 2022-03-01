from collections import Counter
import os
from typing import Optional
from typing import List
os.chdir(os.path.dirname(__file__))

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True
        

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    output = open(r'output', 'w')
    
    for i in range(len(input)):
        nums = eval(input[i])
        sol = Solution()
        output.write(str(sol.containsDuplicate(nums)) + '\n')
    output.close()
    
if __name__ == "__main__":
    main()
