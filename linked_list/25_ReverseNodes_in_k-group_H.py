# Refer to 0_ReverseFirst_N_Nodes_of_LinkedList.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: 
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        a = b = head
        for _ in range(k):
            if b is None:
                return head
            b = b.next
        newHead = self.reverseN(a, k)
        head.next = self.reverseKGroup(b, k)
        return newHead

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