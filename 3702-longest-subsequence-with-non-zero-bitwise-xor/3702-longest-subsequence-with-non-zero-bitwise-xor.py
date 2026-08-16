class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        # Check if the array contains only zeros
        if all(x == 0 for x in nums):
            return 0
            
        # Calculate total XOR sum
        total_xor = 0
        for num in nums:
            total_xor ^= num
            
        # If total XOR is non-zero, take all elements. Otherwise, remove one.
        return len(nums) if total_xor != 0 else len(nums) - 1

        