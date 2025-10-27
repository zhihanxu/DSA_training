# Solution 1: In-place solution to reverse the words in a string
# Time complexity: O(n), Space complexity: O(n)
class Solution1:
    def reverseWords(self, s: str) -> str:
        l = self.trimSpaces(s)
        self.reverse(l, 0, len(l) - 1)
        self.reverseEachWord(l,)
        # print(l)
        return "".join(l)
    
    def trimSpaces(self, s):
        left, right = 0, len(s) - 1
        while left <= right and s[left] == " ":
            left += 1
        while left <= right and s[right] == " ":
            right -= 1
        
        output = []
        while left <= right:
            if s[left] != " ":
                output.append(s[left])
            elif output[-1] != " ":
                 output.append(s[left])
            left += 1
        return output

    def reverse(self, l, left, right):
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
    
    def reverseEachWord(self, l):
        left = right = 0
        while left < len(l):
            while right < len(l) and l[right] != " ":
                right += 1
            self.reverse(l, left, right - 1)
            left = right + 1
            right += 1
        
# Solution 2: Using built-in functions
class Solution2:
    def reverseWords(self, s: str) -> str:
        # return " ".join(reversed(s.split()))
        words = s.split()
        words.reverse()
        # print(words)
        return " ".join(words)

# Test cases
s = "  hello world!  "
solution1 = Solution1()
print(solution1.reverseWords(s))  # Output: "world! hello"
solution2 = Solution2()
print(solution2.reverseWords(s))  # Output: "world! hello"