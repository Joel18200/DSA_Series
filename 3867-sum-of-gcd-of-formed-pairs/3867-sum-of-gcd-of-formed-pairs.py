import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd=[]
        mx=0
        for num in nums:
            mx=max(num,mx)
            value=math.gcd(num,mx)
            prefix_gcd.append(value)
        prefix_gcd.sort()    
        left=0
        right=len(nums)-1
        resultant_sum=0
        while (left<right):
            resultant_sum+=math.gcd(prefix_gcd[left],prefix_gcd[right])
            left+=1
            right-=1
        return resultant_sum    




        