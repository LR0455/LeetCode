from collections import Counter
import os
os.chdir(os.path.dirname(__file__))

def findPairs(nums: list[int], k: int) -> int:
    counter = Counter(nums)
    if k == 0:
        return len(list(filter(lambda x: counter[x] > 1, counter)))
        
    nums = list(set(nums))
    min_num = abs(min(nums))
    nums = list(map(lambda x: x+min_num, nums))
    plus_nums = list(map(lambda x: x+k, nums))
    
    ans = 0
    for num in plus_nums:
        if num in nums:
            ans += 1
    
    return ans

def main():   
    input = open(r'input', 'r')
    input = input.readlines()
    
    nums = eval(input[0])
    k = eval(input[1])
    output = open(r'output', 'w')
    output.write(str(findPairs(nums, k)))
    output.close()
    
if __name__ == "__main__":
    main()
