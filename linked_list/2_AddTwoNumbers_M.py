# Task: Add two numbers stored in reversed order in linked lists.
# Idea: perform the addition node by node, taking care of the carry.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        dummy = ListNode(-1)
        p = dummy

        carry = 0
        while p1 or p2 or carry > 0:
            val = carry
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            carry = val // 10
            res = val % 10
            p.next = ListNode(res)
            p = p.next
        return dummy.next        