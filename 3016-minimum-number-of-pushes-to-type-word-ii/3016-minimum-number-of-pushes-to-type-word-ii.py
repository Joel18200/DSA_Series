from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        count=Counter(word)
        freq=sorted(count.values(),reverse=True)
        res=0
        for i in range(len(freq)):
            pushes=i//8+1
            res+=pushes*freq[i]
        return res    


        