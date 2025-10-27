from typing import List

class Solution1_1:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        slow = fast = 0
        count = 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            elif slow < fast and count < 2:
                slow += 1
                nums[slow] = nums[fast]     
            fast += 1
            count += 1
            if fast < len(nums) and nums[fast] != nums[fast - 1]:
                count = 0
        return slow + 1

# Easier to understand
class Solution1_2:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        slow = 0
        count = 1
        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                count = 1
                slow += 1
                nums[slow] = nums[fast]
            elif count < 2:
                count += 1
                slow += 1
                nums[slow] = nums[fast]     
        return slow + 1

# Example usage:
solution = Solution1_2()
nums = [0,0,0,1,1,1,1,2,3,3]
length = solution.removeDuplicates(nums)
print(length)  # Output: 7
print(nums[:length])  # Output: [0,0,1,1,2,3,3]