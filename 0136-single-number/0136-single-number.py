from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=Counter(nums)
        for num,val in count.items():
            if val==1:
                return num


        