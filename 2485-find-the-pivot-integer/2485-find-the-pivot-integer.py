class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum=n*(n+1)//2
        pivot=int(math.isqrt(total_sum))
        return pivot if pivot*pivot == total_sum else -1
                



        