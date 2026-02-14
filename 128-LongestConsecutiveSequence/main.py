class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        max_seq = -1
        curr_seq = 0
        for num in s:
            if (num - 1) in s: continue

            right = num + 1
            while right in s:
                curr_seq += 1
                right += 1

            if curr_seq > max_seq:
                max_seq = curr_seq

            curr_seq = 0

        return max_seq + 1
