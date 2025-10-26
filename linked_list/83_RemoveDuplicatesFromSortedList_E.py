# Similar to 26_RemoveDuplicatesFromSortedArray_E.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        fast = slow = head
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
            
        # 断开与后面重复元素的连接
        slow.next = None
        return head