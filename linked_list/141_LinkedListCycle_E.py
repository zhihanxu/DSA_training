# Task: Detect a cycle in a linked list.
# Idea: Use two pointers: fast and slow

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
    
if __name__ == "__main__":
    # Creating a linked list with a cycle for testing
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next  # Creating a cycle here

    solution = Solution()
    print(solution.hasCycle(head))  # Output: True