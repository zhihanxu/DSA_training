# Similar to 151 Reverse Words in a String
# Reverse the whole list, then reverse first k nodes, then reverse the rest n-k nodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        k = k % n

        # Important:
        if k == 0:
            return head

        # reverse whole list
        head = self.reverseList(head)
        # reverse first k nodes
        newHead, rest = self.reverseK(head, k)
        tail = head
        # reverse the rest of nodes and connect
        tail.next = self.reverseList(rest)
        return newHead
        
    def reverseList(self, head):
        pre, cur, nxt = None, head, head.next
        while cur:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt:
                nxt = nxt.next
        return pre
    
    def reverseK(self, head, k):
        pre, cur, nxt = None, head, head.next
        while k > 0:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt:
                nxt = nxt.next  
            k -= 1
        return pre, cur
    