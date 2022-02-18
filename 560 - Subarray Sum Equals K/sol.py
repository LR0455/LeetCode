from collections import Counter
import os
os.chdir(os.path.dirname(__file__))

def subarraySum(nums: list[int], k: int) -> int:
    counter = Counter([0])
    ans = 0
    sum_ = 0
    for i in range(len(nums)):
        sum_ += nums[i]
        if counter[sum_ - k] > 0:
            ans += counter[sum_ - k]
        counter[sum_] += 1
        
    return ans

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    
    nums = eval(input[0])
    k = eval(input[1])
    output = open(r'output', 'w')
    output.write(str(subarraySum(nums, k)))
    output.close()
    
if __name__ == "__main__":
    main()
