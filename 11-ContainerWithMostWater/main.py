class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l: int = 0
        r: int = len(heights) - 1

        max_area: int = 0
        while l < r:
            left_height = heights[l]
            right_height = heights[r]
            curr_area = (r - l)

            if left_height < right_height:
                curr_area *= left_height
                l += 1
            else:
                curr_area *= right_height
                r -= 1

            if curr_area > max_area:
                max_area = curr_area

        return max_area
