class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        holder=None
        count=0
        for num in nums:
            if count==0:
                holder=num
            if holder==num:
                count+=1
            else:
                count-=1
        return holder                