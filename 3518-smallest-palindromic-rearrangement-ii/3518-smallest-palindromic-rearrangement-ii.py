from collections import Counter
from math import factorial
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq=Counter(s)
        half={}
        mid=""
        for ch in sorted(freq):
            if freq[ch]%2==1:
                mid=ch
            half[ch]=freq[ch]//2
        total_half=sum(half.values())

        def count_prem():
            remaining = sum(half.values())
            ways = 1

            for cnt in half.values():
                if cnt == 0:
                    continue

                ways *= comb(remaining, cnt)

                if ways >= k:
                    return k
                remaining -= cnt
            return ways
        if count_prem()<k:
            return ""
        first=[]
        while len(first)<total_half:
            for ch in sorted(half):
                if half[ch]==0:
                    continue
            
                half[ch]-=1
                cnt=count_prem()
                if k<=cnt:
                    first.append(ch)
                    break
                else:
                    k-=cnt
                    half[ch]+=1
        first="".join(first)
        return first+mid+first[::-1]        

