import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1: using a priority queue (implemented with min-heap - default of heapq)
# time complexity: O(N log k), space complexity: O(k)
# where k is the number of linked lists, and N is the total number of nodes     
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        pq = [] # priority queue: min heap

        # add head of each list to the priority queue
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, i, head))
        
        while pq:
            val, i, node = heapq.heappop(pq) # get the smallest node
            p.next = node
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))
            p = p.next
        
        return dummy.next

# Solution 2: Merge with Divide and Conquer
