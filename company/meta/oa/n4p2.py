# Q4: given a list of integers, return the number of unique pairs that 
# (1) have the same length (2) differ by only one digit. 
# https://www.reddit.com/r/leetcode/comments/v5ckp1/codesignal_pairs_that_contain_the_same_number_of/

def count_differ_one_digit_pair(nums):
    def check_one_digit_differ(l1, l2):
        assert len(l1) == len(l2)
        count = 0
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                count += 1
        if count == 1:
            return True
        return False
    
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            l1 = str(nums[i])
            l2 = str(nums[j])
            if len(l1) == len(l2):
                if check_one_digit_differ(l1, l2):
                    count += 1
    return count
            
nums = [123, 124, 125, 223, 133, 12, 13, 45]
print(count_differ_one_digit_pair(nums))
# Explanation:
# (123,124), (123,125), (124,125), (123,223), (123,133), (12,13)
# => 6 pairs
# Output: 6