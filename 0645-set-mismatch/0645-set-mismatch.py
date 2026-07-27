from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length=len(nums)
        current_sum=sum(nums)
        non_duplicate_sum=sum(set(nums))
        orginal_sum=length*(length+1)//2
        return [current_sum-non_duplicate_sum,orginal_sum-non_duplicate_sum]

        