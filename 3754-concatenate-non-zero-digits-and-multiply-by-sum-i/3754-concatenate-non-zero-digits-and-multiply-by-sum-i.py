class Solution:
    def sumAndMultiply(self, n: int) -> int:
       s=0
       m=0
       place=1
       if n==0:
        return 0
       while(n>0):
        digit=n%10
        s+=digit
        if digit!=0:
            m+=digit*place
            place*=10
        n//=10
       return m*s    
              

        