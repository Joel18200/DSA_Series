import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        gcd=math.gcd(nums[0],nums[-1])
        return gcd