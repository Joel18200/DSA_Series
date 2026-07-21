class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones=s.count('1')
        t='1'+s+'1'
        len_zero=[len(part) for part in t.split('1') if part]
        if len(len_zero)<2:
            return total_ones
        max_gain=0
        for i in range(len(len_zero)-1):
            current_gain=len_zero[i]+len_zero[i+1]
            max_gain=max(max_gain,current_gain)
        return total_ones+max_gain    
        
        


