import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini=min(nums)
        maxi=max(nums)
        gcd=math.gcd(mini,maxi)
        return gcd