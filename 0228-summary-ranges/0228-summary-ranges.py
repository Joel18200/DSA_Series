class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        if not nums:
            return []
        start=nums[0]
        for i in range(len(nums)-1):
            if nums[i+1]!=nums[i]+1:
                end=nums[i]
                if start==end:
                    res.append(f"{start}")
                else:
                    res.append(f"{start}->{end}")    
                start=nums[i+1] 
        end=nums[-1]
        if start==end:
            res.append(f"{start}")
        else:
            res.append(f"{start}->{end}") 

        return res      



        