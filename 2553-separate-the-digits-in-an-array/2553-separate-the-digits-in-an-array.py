class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        new=[]
        for i in nums:
            for j in str(i):
                new.append(int(j))
        return new        
        