# list of strings
# 求每个str 是另一个str 的前缀，有几个是另一个str的前缀
# 相等只算一次
# （暴力解会超过时间限制
# Example
# arr=[“a”, “a”, “ab”, “abc”, “ac”]
# res = 8

def count_prefixes(arr):
    prefix_count = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j].startswith(arr[i]):
                prefix_count += 1
    return prefix_count

# Example usage:
arr = ["a", "a", "ab", "abc", "ac"]
result = count_prefixes(arr)
print(result)  # Output: 8