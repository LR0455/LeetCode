from collections import Counter
import os
from typing import Optional

os.chdir(os.path.dirname(__file__))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ptr = head
        while list1 and list2:
            if list1.val > list2.val:
                ptr.next = list2
                list2 = list2.next
            else:
                ptr.next = list1
                list1 = list1.next
            ptr = ptr.next
        if list1:
            ptr.next = list1
        if list2:
            ptr.next = list2
        return head.next
def toListNode(arr: list) -> ListNode:
    head = ListNode()
    ptr = head
    for ln in arr:
        ptr.next = ListNode(ln)
        ptr = ptr.next
    return head.next
        
def main():
    input = open(r'input', 'r')
    input = input.readlines()
    output = open(r'output', 'w')
    
    for i in range(0, len(input), 2):
        sol = Solution()
        ptr = sol.mergeTwoLists(toListNode(eval(input[i])), toListNode(eval(input[i+1])))
        res = []
        while ptr:
            res.append(ptr.val)
            ptr = ptr.next

        output.write(str(res))
    output.close()
    
if __name__ == "__main__":
    main()
