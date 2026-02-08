class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l = len(nums)
        prefix = 1
        products = [1] * l
        for i in range(l):
            products[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(l - 1, -1, -1):
            products[i] *= postfix
            postfix *= nums[i]

        return products
