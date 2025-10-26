# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1: Iterative: require three pointers to reverse
# Space: O(1)
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev, curr, nxt = None, head, head.next
        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            if nxt:
                nxt = nxt.next
        return prev

# Solution 2: Recursive: remember base case
# Space: O(n) for recursion stack
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head is None or head.next is None:
            return head
        
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last