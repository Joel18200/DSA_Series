class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=max(nums)
        count=0
        temp=[]

        for i in nums:
            if i==n:
                count+=1
            else:
                temp.append(i)
        temp.sort()          
        if count==2 and temp==list(range(1,n)):
            return True
        return False          
        