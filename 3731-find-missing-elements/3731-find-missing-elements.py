class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s=set(nums)
        res=[]
        min_element,max_element=min(nums),max(nums)
        for num in range(min_element,max_element+1):
            if num not in s:
                res.append(num)
        return res  
        

        