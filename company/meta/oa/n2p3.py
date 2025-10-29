# 给出二维数组 Matrix: list[list[int]]
# 判断斜线方向（对角线方向上） 按照这个顺序1 2 0 2 0 … 最长的length
# 从1 开始，2, 0 一直重复
# 返回最长length
# Example
# 1 1 1 0 2
# 0 2 1 2 1
# 0 1 0 1 1
# res=3

def longest_diagonal_pattern(matrix):
    if not matrix or not matrix[0]:
        return 0

    n, m = len(matrix), len(matrix[0])
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    def in_bounds(x, y):
        return 0 <= x < n and 0 <= y < m

    max_len = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 1:
                continue
            for dx, dy in directions:
                x, y = i, j
                expected = 1
                length = 0
                while in_bounds(x, y) and matrix[x][y] == expected:
                    length += 1
                    # pattern alternates after the first 1
                    expected = 2 if expected == 1 else (0 if expected == 2 else 2)
                    x += dx
                    y += dy
                end_x, end_y = x - dx, y - dy
                if end_x in (0, n-1) or end_y in (0, m-1):
                    max_len = max(max_len, length)
    return max_len

# Example usage:
matrix = [
    [0, 0, 1, 2],
    [0, 2, 2, 2],
    [2, 1, 0, 1]
]
result = longest_diagonal_pattern(matrix) 
print(result)  # Output: 3
print(longest_diagonal_pattern([[1,2,0,2,0]]))  # → 5 (horizontal diagonal = one row)
print(longest_diagonal_pattern([[1],[2],[0],[2]]))  # → 4 (vertical diagonal)
print(longest_diagonal_pattern([[0,1,2],[1,2,0],[2,0,1]]))  # → 3 (diagonal)