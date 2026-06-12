class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i=0
        asc=True
        desc=True
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                asc=False
            if nums[i]>nums[i+1]:
                desc=False 
        return asc or desc                      

