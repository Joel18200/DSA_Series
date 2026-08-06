class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            ans=1
            for ch in str(n):
                ans*=int(ch)
            if ans%t==0:
                return n
                break
            n+=1