# Idea: Binary Search - find the minimum eating speed x such that f(x) == h
# x is the eating speed, f(x) is the hours needed to eat all bananas with speed x

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        # right = 10**9
        right = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            if self.f(piles, mid) <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def f(self, piles, x):
        hours = 0
        for pile in piles:
            hours += pile // x
            if pile % x > 0:
                hours += 1
        return hours
    