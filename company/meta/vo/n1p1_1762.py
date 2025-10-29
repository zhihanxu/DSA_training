# 假设数组最左边靠近陆地，最右边靠海，数组里面的每个元素代表建筑高度，如果一个建筑比右边的都高，那它就能看到海，返回有多少建筑能看到海
# 1762. Buildings With an Ocean View


# iterative:
class Solution1:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [n - 1]
        tallest = heights[n - 1]
        for i in range(n - 2, -1, -1):
            if heights[i] > tallest:
                res.insert(0, i)
                tallest = heights[i]
        return res
    
# monotonic stack:
class Solution2:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = []
        
        # Monotonically decreasing stack.
        stack = []
        for current in reversed(range(n)):
            # If the building to the right is smaller, we can pop it.
            while stack and heights[stack[-1]] < heights[current]:
                stack.pop()
            
            # If the stack is empty, it means there is no building to the right 
            # that can block the view of the current building.
            if not stack:
                answer.append(current)
            
            # Push the current building in the stack.
            stack.append(current)
        
        answer.reverse()
        return answer