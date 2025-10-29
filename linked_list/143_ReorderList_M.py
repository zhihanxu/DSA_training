from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1: Find middle, reverse second half, then merge two halves
# 快慢指针，反转链表，合并链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        # pre, cur, nxt = None, slow, slow.next
        # while cur:
        #     cur.next = pre
        #     pre = cur
        #     cur = nxt
        #     if nxt:
        #         nxt = nxt.next
        #                 prev, curr = None, slow
        
        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        # p1, p2 = head, pre
        # while p2.next:
        #     tmp = p1.next
        #     p1.next = p2
        #     p1 = tmp
        #     tmp = p2.next
        #     p2.next = p1
        #     p2 = tmp
            
# Solution 2: Use stack to store all nodes, then reorder
# Be careful about the stopping condition, and avoid the cycle
# The step is like reducing a large cycle to a small cycle until break (no cycle)
class Solution2:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p = head
        stk = []

        while p:
            stk.append(p)
            p = p.next
        
        p = head
        while p:
            nxt = p.next
            lastNode = stk.pop()
            if lastNode == nxt or lastNode.next == nxt:
                lastNode.nxt = None
                break
            p.next = lastNode
            lastNode.next = nxt
            p = nxt