# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Solution 1: intuitive: fast-slow pointers, fast pointer explore duplicates, slow pointer build the new list
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p, q = dummy, head

        while q:
            if q.next and q.val == q.next.val:
                q = q.next
                while q.next and q.val == q.next.val:
                    q = q.next
                q = q.next
            else:
                p.next = q
                p = p.next
                q = q.next
        return dummy.next
    
# Solution 2: reommended: linked list partition method: one list storing duplicates, the other storing uniques
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummyUniq = ListNode(101)
        dummyDup = ListNode(101)

        pUniq, pDup = dummyUniq, dummyDup
        p = head

        while p:
            if (p.next and p.val == p.next.val) or p.val == pDup.val:
                pDup.next = p
                pDup = pDup.next
            else:
                pUniq.next = p
                pUniq = pUniq.next

            p = p.next
            pUniq.next = None
            pDup.next = None

        return dummyUniq.next