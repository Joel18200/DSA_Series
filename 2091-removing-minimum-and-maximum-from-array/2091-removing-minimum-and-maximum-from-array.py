class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        max_element=max(nums)
        min_element=min(nums)
        max_index=nums.index(max_element)
        min_index=nums.index(min_element)
        left = min(max_index,min_index)
        right = max(max_index,min_index)
        n=len(nums)
        both_left=right+1
        both_right = n-left
        left_right = left+1+n-right
        return min(both_left, both_right, left_right)
        