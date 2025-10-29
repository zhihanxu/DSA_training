from queue import PriorityQueue
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = PriorityQueue()

        for i in range(len(nums1)):
            pq.put((nums1[i] + nums2[0], i, 0)) 
        
        res = []
        while pq and k > 0:
            s, i, j = pq.get()
            k -= 1
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                pq.put((nums1[i] + nums2[j + 1], i, j + 1))
        return res

# time complexity O(k log n), space complexity O(n)

# Example usage:
if __name__ == "__main__":
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    solution = Solution()
    result = solution.kSmallestPairs(nums1, nums2, k)
    print(result)  # Output: [[1,2],[1,4],[1,6]]