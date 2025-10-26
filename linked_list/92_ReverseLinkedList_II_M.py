# The solution is based on 0_ReverseFirst_N and 206_ReverseLinkedList


# Solution 1: Iterative
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverseN(head, right)
        
        pre = head
        for _ in range(1, left - 1):
            pre = pre.next
        pre.next = self.reverseN(pre.next, right - left + 1)
        return head
        
    # from 0_ReverseFirst_N
    def reverseN(self, head, n):
        if head is None or head.next is None:
            return head
        pre, cur, nxt = None, head, head.next
        while n > 0:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt:
                nxt = nxt.next
            n -= 1
        head.next = cur
        return pre

# Solution 2: Recursive
class Solution2:
    def __init__(self):
        # 后驱节点
        self.successor = None

    def reverseBetween(self, head, m, n):
        # base case
        if m == 1:
            return self.reverseN(head, n)
        # 前进到反转的起点触发 base case
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

    # 反转以 head 为起点的 n 个节点，返回新的头结点
    # from 0_ReverseFirst_N
    def reverseN(self, head, n):
        if n == 1:
            # 记录第 n + 1 个节点
            self.successor = head.next
            return head

        last = self.reverseN(head.next, n - 1)

        head.next.next = head
        head.next = self.successor
        return last