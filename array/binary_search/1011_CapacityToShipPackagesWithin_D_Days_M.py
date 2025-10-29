# Task:     
    # x: cap, f(x): days needed
    # find smallest x such that f(x) <= days
    
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = left + (right - left) // 2
            if self.f(weights, mid) <= days:
                right = mid - 1
            else:
                left = mid + 1
        return left

    # Accumulate weights until exceeding cap
    def f(self, weights, x):
        days = 1    # important: always at least one day
        partial = 0
        for weight in weights:
            if partial + weight <= x:
                partial += weight
            else:
                days += 1
                partial = weight    # important
        return days
    
    # Compare each new weight with remaining cap
    # def f(self, weights, x):
    #     days = 0
    #     i = 0
    #     while i < len(weights):
    #         cap = x
    #         while i < len(weights):
    #             if cap >= weights[i]:
    #                 cap -= weights[i]
    #                 i += 1
    #             else:
    #                 break
    #         days += 1
    #     return days