from collections import Counter
import os
from typing import List
os.chdir(os.path.dirname(__file__))
class Solution:
    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remaining_gas = list(map(lambda x: x[0]-x[1], zip(gas, cost)))
        if (sum(remaining_gas) < 0):
            return -1
        
        start = 0
        sum_ = 0
        for i in range(len(remaining_gas)):
            sum_ += remaining_gas[i]
            if (sum_ < 0):
                start = i + 1
                sum_ = 0
                
        return start

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    
    gas = eval(input[0])
    cost = eval(input[1])
    
    output = open(r'output', 'w')
    sol = Solution()
    output.write(str(sol.canCompleteCircuit(gas, cost)))
    output.close()
    
if __name__ == "__main__":
    main()
