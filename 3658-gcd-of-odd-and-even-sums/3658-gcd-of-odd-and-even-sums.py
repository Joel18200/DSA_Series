import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd=0
        sum_even=0
        count=0
        for i in range(1,(n*2)+1):
            if i%2!=0:
                sum_odd+=i
            else:
                sum_even+=i
        result=math.gcd(sum_even,sum_odd)
        return result            


        