class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_value=nums[0]
        value=nums[0]
        for num in nums[1:]:
            value=max(num+value,num)
            max_value=max(max_value,value)
        return max_value
