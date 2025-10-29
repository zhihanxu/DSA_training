# 680. Valid Palindrome II

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s[left + 1 : right + 1]) or self.isPalindrome(s[left : right])
            left += 1
            right -= 1
        return True 
                
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
# Test
s = "eceec"
print(Solution().validPalindrome(s))    # instance method calling with self
