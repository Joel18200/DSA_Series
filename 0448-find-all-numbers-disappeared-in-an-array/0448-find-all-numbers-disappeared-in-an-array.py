class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set=set(nums)
        n=len(nums)
        res=[]
        for i in range(1,n+1):
            if i not in num_set:
                res.append(i)
        return res


        