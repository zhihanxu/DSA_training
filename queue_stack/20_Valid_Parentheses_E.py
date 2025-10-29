class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stk = []
        for c in s:
            if c in "({[":
                stk.append(c)
            else:
                if stk and stk[-1] == mapping[c]:
                    stk.pop()
                else:
                    return False
        return not stk  # important to check if stack is empty at the end