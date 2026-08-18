class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        s=Counter(nums)
        validate=[]
        #Case:1
        if len(nums)==k:
            return max(nums)
        #Case:2
        if k==1:
            unique_ele=[num for num in nums if s[num]==1]
            return max(unique_ele) if unique_ele else -1
        #Case:3
        num1=nums[0]
        num2=nums[-1]
        if s[num1]==1:
            validate.append(num1)
        if s[num2]==1:
            validate.append(num2)
        return max(validate) if validate else -1
        