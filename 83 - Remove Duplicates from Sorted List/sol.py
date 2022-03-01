from collections import Counter
import os
from typing import Optional
from typing import List
os.chdir(os.path.dirname(__file__))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        ptr, nxt = head, head.next
        
        while nxt:
            if ptr.val == nxt.val:
                ptr.next = nxt.next
            else:
                ptr = ptr.next
            nxt = nxt.next
            
        return head
        
    
def main():
    input = open(r'input', 'r')
    input = input.readlines()
    output = open(r'output', 'w')
    
    for i in range(len(input)):
        arr = eval(input[i])
        head = ListNode()
        ptr = head
        for num in arr:
            ptr.next = ListNode(num)
            ptr = ptr.next
            
        sol = Solution()
        ptr = sol.deleteDuplicates(head.next)
        res = []
        while ptr:
            res.append(ptr.val)
            ptr = ptr.next
        output.write(str(res) + '\n')
    output.close()
    
if __name__ == "__main__":
    main()
