from collections import Counter
import os
from typing import Optional
from typing import List
os.chdir(os.path.dirname(__file__))

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged_arr = [0 for _ in range(m+n)]
        i, j, k = 0, 0, 0
        while i < m or j < n:
            if i == m:
                merged_arr[k] = nums2[j]
                j += 1
            elif j == n or nums1[i] < nums2[j]:
                merged_arr[k] = nums1[i]
                i += 1
            else:
                merged_arr[k] = nums2[j]
                j += 1
            k += 1
        
        for i in range(m+n):
            nums1[i] = merged_arr[i]

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    output = open(r'output', 'w')
    
    for i in range(0, len(input), 4):
        nums1 = eval(input[i])
        m = eval(input[i+1])
        nums2 = eval(input[i+2])
        n = eval(input[i+3])
        sol = Solution()
        sol.merge(nums1, m, nums2, n)

        output.write(str(nums1) + '\n')
    output.close()
    
if __name__ == "__main__":
    main()
