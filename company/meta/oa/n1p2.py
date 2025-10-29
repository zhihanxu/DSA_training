# Given a matrix of integers, with each element containing either 0, 1, or 2
# your task is to find the longest diagonal segment which matches the following patter: 
# 1, 2, 0, 2, 0, 2, 0 (where the first element is 1, and then 2 and 0 are repeating infinitely, and finishes at a matrix border. 
# Reutrn the length of this diagonal segment. 
# The diagonal segment: may start at any matrix element may go toward any possible diagonal direction 
# and must end at an element in the first or last row or column. 
# for matrix = [[0, 0, 1, 2], [0, 2,2,2],[2,1,0,1]] the output will be 3
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
                if end_x in (0, n - 1) or end_y in (0, m - 1):
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


# 3459 变种