# Array Problems

只要数组有序，就应该想到双指针技巧

```cpp
// 滑动窗口算法框架伪码
int left = 0, right = 0;
while (right < nums.size()) {
    // 增大窗口
    window.addLast(nums[right]);
    right++;
    while (window needs shrink) {
        // 缩小窗口
        window.removeFirst(nums[left]);
        left++;
    }
}

```python
def binarySearch(nums: List[int], target: int) -> int:
    # 一左一右两个指针相向而行
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1