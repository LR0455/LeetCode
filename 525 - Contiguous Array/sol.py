from collections import Counter
import os
os.chdir(os.path.dirname(__file__))

def findMaxLength(nums: list[int]) -> int:
    nums = [x if x == 1 else -1 for x in nums]
    
    pos, sum_, ans = {}, 0, 0
    for i in range(len(nums)):
        sum_ += nums[i]
        if sum_ == 0:
            ans = i+1
        elif sum_ in pos:
            ans = max(ans, i - pos[sum_])
        else:
            pos[sum_] = i
    return ans
        

def main():   
    input = open(r'input', 'r')
    input = input.readlines()
    
    nums = eval(input[0])
    output = open(r'output', 'w')
    output.write(str(findMaxLength(nums)))
    output.close()
    
if __name__ == "__main__":
    main()
