class Solution:
    def isPalindrome(self, s: str) -> bool:
        sb = []
        for c in s:
            if c.isalnum():
                sb.append(c.lower())
        
        s = "".join(sb)
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
    
# Space O(1) solution
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True