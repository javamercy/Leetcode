class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack: list[tuple[int, int]] = []
        largest_area = 0

        for i, height in enumerate(heights):
            popped_index = i
            if not stack or stack[-1][1] <= height:
                stack.append((i, height))
                continue

            while stack and height < stack[-1][1]:
                popped = stack.pop()
                curr_area = (i - popped[0]) * popped[1]
                if curr_area > largest_area:
                    largest_area = curr_area

                popped_index = popped[0]

            stack.append((popped_index, height))

        for index, height in stack:
            curr_area = height * (len(heights) - index)
            if curr_area > largest_area:
                largest_area = curr_area

        return largest_area
