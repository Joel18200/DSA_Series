class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        for select_index in range(len(nums)):
            select_value=nums[select_index]
            count=0
            for index,value in enumerate(nums):
                if index==select_index:
                    continue
                if value<select_value:
                    count+=1
            result.append(count)
        return result            
                

        