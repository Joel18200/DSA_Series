class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        num_set=set(nums)
        su=nums[0]
        curr=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==curr+1:
                curr=nums[i]
                su+=curr
            else:
                break
        while su in num_set:
            su+=1
        return su

            



                
        