
# Task: Find the k-th smallest element in a sorted matrix.
# Similar solution with 23: Merge K Sorted Lists
from queue import PriorityQueue

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = PriorityQueue()

        for i in range(len(matrix)):
            pq.put((matrix[i][0], i, 0))

        while pq and k > 0:
            cur = pq.get()
            k -= 1
            res = cur[0]
            i, j = cur[1], cur[2]
            if j + 1 < len(matrix):
                pq.put((matrix[i][j+1], i, j + 1))
        return res

# min heap is based on binary heap, both put() and get() are O(log n)
# time complexity O(k log n), space complexity O(n)