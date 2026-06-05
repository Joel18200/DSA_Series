class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t)
        window={}
        need_count=len(need)
        have=0
        left=0
        res=""
        min_len=float('inf')
        for right in range(len(s)):
            ch=s[right]
            window[ch]=window.get(ch,0)+1
            if ch in need and window[ch]==need[ch]:
                have+=1
            while have==need_count:
                if right-left+1<min_len:
                    min_len=right-left+1
                    res=s[left:right+1]
                window[s[left]]-=1
                if s[left] in need and window[s[left]]<need[s[left]]:
                    have-=1
                left+=1
        return res            

        