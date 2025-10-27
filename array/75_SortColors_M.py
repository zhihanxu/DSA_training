# Can refer to 283 and 27, but requiring multiple pass
# Here is a one-pass solution using three pointers

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [0, p0) for 0, (p2, len(nums) - 1] for 2
        p0, p, p2 = 0, 0, len(nums) - 1
        while p <= p2:
            if nums[p] == 0:
                self.swap(nums, p, p0)
                p0 += 1
                p += 1  # Method 1: need to move p forward here
            elif nums[p] == 2:
                self.swap(nums, p, p2)
                p2 -= 1
            else:
                p += 1
            
            # Method 2: alternative way to handle p increment
            # if p < p0:
            #     p = p0

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]