# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1: fast-slow pointer to split two half + reverse right half
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        if fast:
            slow = slow.next

        left = head
        right = self.reverse(slow)
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
    
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        pre, cur, nxt = None, head, head.next
        while cur:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt:
                nxt = nxt.next
        return pre

# Solution 2: Recursive + 后续遍历
class Solution2:
    def __init__(self):
        self.left = None
        self.res = True

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head
        self.traversal(head)
        return self.res

    def traversal(self, right: ListNode):
        if right is None:
            return
        
        self.traversal(right.next)

        # 后续遍历
        if self.left.val != right.val:
            self.res = False
        self.left = self.left.next