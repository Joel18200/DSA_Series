class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        pos1=pos2=pos3=float('-inf')
        neg1=neg2=float('inf')
        for n in nums:
            if n>pos1:
                pos3=pos2
                pos2=pos1
                pos1=n
            elif n>pos2:
                pos3=pos2
                pos2=n
            elif n>pos3:
                pos3=n
            
            if n<neg1:
                neg2=neg1
                neg1=n
            elif n<neg2:
                neg2=n
        return max(pos3*pos2*pos1,neg1*neg2*pos1)        


        