# Task: Add two numbers stored in normal order in linked lists
# Idea: Use stacks to reverse the order of digits for addition

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk1 = []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        stk2 = []
        while l2:
            stk2.append(l2.val)
            l2 = l2.next
        
        dummy = ListNode(-1)

        carry = 0
        while stk1 or stk2 or carry > 0:
            res = carry
            if stk1:
                res += stk1.pop()
            if stk2:
                res += stk2.pop()
            carry = res // 10
            val = res % 10
            newNode = ListNode(val)
            newNode.next = dummy.next
            dummy.next = newNode
            
        return dummy.next
