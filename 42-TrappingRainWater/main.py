class Solution:
    def trap1(self, heights: list[int]) -> int:
        n = len(heights)
        max_left_arr: list[int] = [0] * n
        max_right_arr: list[int] = [0] * n
        max_left: int = 0
        max_right: int = 0
        total: int = 0

        for i in range(n):
            if heights[i] > max_left:
                max_left = heights[i]

            max_left_arr[i] = max_left

            if heights[n - i - 1] > max_right:
                max_right = heights[n - i - 1]

            max_right_arr[n - i - 1] = max_right

        for i, height in enumerate(heights):
            l = max_left_arr[i]
            r = max_right_arr[i]

            if l < r:
                total += l - height
            else:
                total += r - height

        return total

    def trap2(self, heights: list[int]) -> int:
        max_left: int = 0
        max_right: int = 0
        total: int = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            if heights[l] > max_left:
                max_left = heights[l]

            if heights[r] > max_right:
                max_right = heights[r]

            if max_left < max_right:
                total += max_left - heights[l]
                l += 1
            else:
                total += max_right - heights[r]
                r -= 1

        return total
