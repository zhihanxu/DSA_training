from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def findFromEnd(self, head, n):
        p1 = head
        p2 = head
        
        for _ in range(n):
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        x = self.findFromEnd(dummy, n + 1)
        x.next = x.next.next
        return dummy.next

# Example usage:
if __name__ == "__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    n = 2
    solution = Solution()
    new_head = solution.removeNthFromEnd(head, n)

    # Print the modified linked list
    p = new_head
    while p:
        print(p.val, end=" -> " if p.next else "\n")
        p = p.next
    # Output: 1 -> 2 -> 3 -> 5



