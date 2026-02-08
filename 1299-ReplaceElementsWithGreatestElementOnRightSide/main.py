class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        right_max = -1
        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            arr[i] = right_max
            if curr > right_max:
                right_max = curr
        return arr
