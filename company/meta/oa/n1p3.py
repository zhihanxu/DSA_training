# Q4: In the shadowy circuits of the hacker underworld, data isn't just stored, it's encoded with secrets. 
# Among the lines of encrypted entries lies an array of codes (represented by positive integers), each one a digital fingerprint. 
# within this set, certain code-pairs appear nearly identical, save for a subtle corruption in a single digit. 
# you've intercepted this array and you mission is to uncover how many unique index-pairs (i,j) exist such that 0 <= i < j < codes.length, 
# where the codes are exactly the same length, but differ in precisely one digit. 
# for codes = [404, 12, 504, 7, 414, 604, 700, 1] the output will be 5

def count_one_digit_diff_pairs(codes):
    # Convert all numbers to strings
    str_codes = [str(c) for c in codes]

    # Group by length (no defaultdict)
    groups = {}
    for s in str_codes:
        l = len(s)
        if l not in groups:
            groups[l] = []
        groups[l].append(s)

    # Helper: check if two codes differ by exactly one digit
    def differ_by_one(a, b):
        diff = 0
        for x, y in zip(a, b):
            if x != y:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1

    # Count valid pairs
    count = 0
    for same_len_codes in groups.values():
        n = len(same_len_codes)
        for i in range(n):
            for j in range(i + 1, n):
                if differ_by_one(same_len_codes[i], same_len_codes[j]):
                    count += 1
    return count


# Example
codes = [404, 12, 504, 7, 414, 604, 700, 1]
print(count_one_digit_diff_pairs(codes))  # Output: 5
