class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = self.nextGreaterElementInternal(nums2)
        ans = []
        mapping = {}
        for i in range(len(nums2)):
            mapping[nums2[i]] = greater[i]
        for i in range(len(nums1)):
            ans.append(mapping[nums1[i]])
        return ans
    
    def nextGreaterElementInternal(self, nums):
        n = len(nums)
        res = [-1] * n
        # monotonic decreasing stack
        s = []
        for i in range(n - 1, -1, -1):
            while s and s[-1] <= nums[i]:
                s.pop()
            if s:
                res[i] = s[-1]
            s.append(nums[i])
        return res
