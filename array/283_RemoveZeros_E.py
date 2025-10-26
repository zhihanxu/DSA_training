# Task: In-place removal of zeros from an array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = self.removeElement(nums, 0)
        for i in range(p, len(nums)):
            nums[i] = 0
    
    # Helper function from 27
    def removeElement(self, nums, val):
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow