class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            s=str(n)
            ans=1
            for i in range(len(s)):
                conversion=int(s[i])
                ans*=conversion
            if ans%t==0:
                return n
                break
            n+=1