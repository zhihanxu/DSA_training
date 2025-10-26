# fast and slow pointer, similar to 26, 83

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = slow = 0
        for _ in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow