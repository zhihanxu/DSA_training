class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0] * n
        df = self.Difference(nums)
        for booking in bookings:
            i = booking[0] - 1
            j = booking[1] - 1
            val = booking[2]
            df.increment(i, j, val)
        return df.result()
    
    class Difference:
        def __init__(self, nums):
            assert len(nums) > 0
            self.diff = [0] * len(nums)
            self.diff[0] = nums[0]
            for i in range(1, len(nums)):
                self.diff[i] = nums[i] - nums[i - 1]
        
        def increment(self, i, j, val):
            self.diff[i] += val
            if j + 1 < len(self.diff):
                self.diff[j + 1] -= val

        def result(self):
            res = [0] * len(self.diff)
            res[0] = self.diff[0]
            for i in range(1, len(res)):
                res[i] = res[i - 1] + self.diff[i]
            return res
