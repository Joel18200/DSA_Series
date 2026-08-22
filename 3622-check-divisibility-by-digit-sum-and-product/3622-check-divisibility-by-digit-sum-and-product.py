class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum_d=0
        mul_d=1
        d=n
        while n>0:
            s=n%10
            n=n//10
            sum_d+=s
            mul_d*=s
        return d%(sum_d+mul_d)==0