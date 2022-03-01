from collections import Counter
import os
from typing import Optional
from typing import List
os.chdir(os.path.dirname(__file__))

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left
        

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    output = open(r'output', 'w')
    
    for i in range(0, len(input), 2):
        nums = eval(input[0])
        target = eval(input[1])
    
        sol = Solution()
        output.write(str(sol.searchInsert(nums, target)) + '\n')
    output.close()
    
if __name__ == "__main__":
    main()
