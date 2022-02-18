from collections import Counter
import os
os.chdir(os.path.dirname(__file__))

def checkInclusion(s1: str, s2: str) -> bool:
    s1_len = len(s1)
    s1_counter = Counter(s1)
    s2_counter = Counter()
    for i in range(len(s2)):
        s2_counter[s2[i]] += 1
        if i >= s1_len:
            s2_counter[s2[i-s1_len]] -= 1
        if s1_counter == s2_counter:
            return True
        
    return False

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    
    s1, s2 = eval(input[0]), eval(input[1])
    
    output = open(r'output', 'w')
    output.write(str(checkInclusion(s1, s2)))
    output.close()
    
if __name__ == "__main__":
    main()
