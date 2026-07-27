class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i=float('-inf')
        j=float('-inf')
        for num in nums:
            if num>j:
                i=j
                j=num
            elif num>i:
                i=num
        return ((i-1)*(j-1))           

        