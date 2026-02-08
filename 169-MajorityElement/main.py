from collections import Counter


class Solution:
    def majorityElement1(self, nums: list[int]) -> int:
        counts = Counter(nums)
        m = 0
        elem = 0
        for key, value in counts.items():
            if value > m:
                elem = key
                m = value
        return elem

    def majorityElement2(self, nums: list[int]) -> int:
        major = 0
        count = 0
        for num in nums:
            if count == 0:
                major = num
            if num == major:
                count += 1
            else:
                count -= 1

        return major
