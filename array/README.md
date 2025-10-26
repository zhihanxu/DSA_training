# Array Problems

<pre> ```cpp // Pseudo Code for Sliding Window int left = 0, right = 0; while (right < nums.size()) { // Increase Window window.addLast(nums[right]); right++; while (window needs shrink) { // Decrease Window window.removeFirst(nums[left]); left++; } } ``` </pre>
