# Task: In-place removal of duplicates from a sorted array.
# Idea: Use fast-slow pointers: fast pointer explores the array, slow pointer updates the new array

# Similar to 83_RemoveDuplicatesFromSortedList_E.py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        fast = slow = 0
        for _ in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1