class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res=[]
        min_element,max_element=min(nums),max(nums)
        temp=[i for i in range(min_element,max_element+1)]
        for num in temp:
            if num not in nums:
                res.append(num)
        return res  
        

        