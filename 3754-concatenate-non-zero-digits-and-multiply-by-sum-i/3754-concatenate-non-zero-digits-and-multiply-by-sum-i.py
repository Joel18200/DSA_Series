class Solution:
    def sumAndMultiply(self, n: int) -> int:
       a=str(n)
       z=""
       s=0
       for ch in a:
        s+=int(ch)
        if ch!='0':
            z+=ch
       return (int(z) if z else 0) *s   

        