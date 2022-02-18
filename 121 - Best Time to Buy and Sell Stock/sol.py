import os
os.chdir(os.path.dirname(__file__))

def maxProfit(prices: list[int]) -> int:
    ans = 0
    min_stock = 1e9
    for i in range(len(prices)):
        min_stock = min(min_stock, prices[i])
        ans = max(ans, prices[i] - min_stock)
    return ans

def main():
    input = open(r'input', 'r')
    input = input.readlines()
    
    prices = eval(input[0])
    output = open(r'output', 'w')
    output.write(str(maxProfit(prices)))
    output.close()
    
if __name__ == "__main__":
    main()
