from collections import Counter
import os
os.chdir(os.path.dirname(__file__))

def findAnagrams(s: str, p: str) -> list[int]:
    scounter = Counter()
    pcounter = Counter(p)
    plen = len(p)
    ans = []
    for i in range(len(s)):
        scounter[s[i]] += 1
        if i >= plen:
            scounter[s[i-plen]] -= 1
        
        if pcounter == scounter:
            ans.append(i-plen+1)
    return ans
        
def main():   
    input = open(r'input', 'r')
    input = input.readlines()
    
    s = eval(input[0])
    p = eval(input[1])
    output = open(r'output', 'w')
    output.write(str(findAnagrams(s, p)))
    output.close()
    
if __name__ == "__main__":
    main()
