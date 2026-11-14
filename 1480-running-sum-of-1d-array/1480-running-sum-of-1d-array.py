class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        left=[nums[0]]
        sum=nums[0]
        for right in range(1,len(nums)):
            sum+=nums[right]
            left.append(sum)
        return left
            


        