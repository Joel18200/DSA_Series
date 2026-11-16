class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        thresh=len(nums)//3
        cand_1,cand_2=None,None
        count_1,count_2=0,0
        for num in nums:
            if cand_1==num:
                count_1+=1
            elif cand_2==num:
                count_2+=1
            elif count_1==0:
                cand_1=num
                count_1=1
            elif count_2==0:
                cand_2=num
                count_2=1
            else:
                count_1-=1
                count_2-=1
        count_1,count_2=0,0
        result=[]
        for num in nums:
            if num==cand_1:
                count_1+=1
            elif num==cand_2:
                count_2+=1
        if count_1>thresh:
            result.append(cand_1)
        if count_2>thresh:
            result.append(cand_2)
        return result
        
            
        