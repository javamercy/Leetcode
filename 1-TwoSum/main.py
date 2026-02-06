from typing import List


class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:]):
                if num1 + num2 == target:
                    return [i, j + i + 1]
        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            j = d.get(target - num)
            if j is not None:
                return [j, i]
            d[num] = i
        return []
