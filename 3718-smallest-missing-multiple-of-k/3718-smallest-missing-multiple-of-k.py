class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        c=set(nums)
        m=k
        while m in c:
            m+=k
        return m

        


        