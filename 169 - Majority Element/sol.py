from collections import Counter
import os
os.chdir(os.path.dirname(__file__))

def majorityElement(nums: list[int]) -> int:
    count = 0
    num = 0
    for n in nums:
        if (count == 0):
            count = 1
            num = n
        elif (n != num):
            count -= 1
        else:
            count += 1
    
    return num

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    
    nums = eval(input[0])
    
    output = open(r'output', 'w')
    output.write(str(majorityElement(nums)))
    output.close()
    
if __name__ == "__main__":
    main()
