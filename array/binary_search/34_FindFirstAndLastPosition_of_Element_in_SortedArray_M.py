# Tips: 
    # if target not found, left bound is the smallest index x such that f(x) > target
    # right bound is the largest index x such that f(x) < target

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.left_bound(nums, target)
        r = self.right_bound(nums, target)
        return [l, r]

    def left_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid - 1  
        if left < 0 or left >= len(nums):
            return -1
        return left if nums[left] == target else -1
        
    def right_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                left = mid + 1  
        if right < 0 or right >= len(nums):
            return -1
        return right if nums[right] == target else -1