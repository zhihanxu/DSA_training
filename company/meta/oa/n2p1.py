# 给出arr: list[int] 邀请检查arr中连续三个数i, i+1, i+2是否单调递增/递减 
# 返回result: list of 1 or 0, length = len(arr)-2 
# 1: 当前index 对应的后续三个数字连续单调 
# 0: 当前index 对应的后续三个数字不单调 
# Example: arr = [1, 2, 3, 3, 1, 0] res = [1, 0, 0, 1]
def check_monotonic_triplets(arr):
    result = []
    for i in range(len(arr) - 2):
        if (arr[i] < arr[i + 1] < arr[i + 2]) or (arr[i] > arr[i + 1] > arr[i + 2]):
            result.append(1)
        else:
            result.append(0)
    return result