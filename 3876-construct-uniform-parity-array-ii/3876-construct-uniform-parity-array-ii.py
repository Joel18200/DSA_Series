class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd_parity=min(nums1)
        if odd_parity%2!=0:
            return True
        for num in nums1:
            if num%2!=0:
                return False
        return True