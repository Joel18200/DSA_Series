class Solution:
    def romanToInt(self, s: str) -> int:
        op=0
        Map={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for ch in range(len(s)):
            if ch+1<len(s) and Map[s[ch]]<Map[s[ch+1]]:
                op-=Map[s[ch]]
            else:
                op+=Map[s[ch]]
        return op            
            