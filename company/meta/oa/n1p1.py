# Q1: 给了一个string，然后turn lowercase to uppercase and uppercase to lowercase
class Solution1:
    def reverseCase(self, s: str) -> str:
        result = []
        for char in s:
            if char.islower():
                result.append(char.upper())
            elif char.isupper():
                result.append(char.lower())
            else:
                result.append(char)
        return ''.join(result)

# Similar to 709
class Solution2:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for c in s:
            if c.isupper():
                res += c.lower()
            else:
                res += c
        return res

# Test cases
s = "Hello World!"
solution1 = Solution1()
print(solution1.reverseCase(s))  # Output: "hELLO wORLD!"
solution2 = Solution2()
print(solution2.toLowerCase(s))  # Output: "hello world!"