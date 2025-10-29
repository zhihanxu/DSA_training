# Exactly the same as 1011

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # x: largest sum
        # f(x): required splits
        # find smallest x such that f(x) == k
        
        left = max(nums)
        right = sum(nums)
        
        while left <= right:
            mid = left + (right - left) // 2
            if self.f(nums, mid) <= k:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def f(self, nums, x):
        splits = 0
        i = 0
        while i < len(nums):
            largest_sum = x
            while i < len(nums):
                if nums[i] <= largest_sum:
                    largest_sum -= nums[i]
                    i += 1
                else:
                    break
            splits += 1
        return splits