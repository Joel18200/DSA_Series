class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        
        left_sum = sum(int(c) for c in num[:mid] if c != '?')
        right_sum = sum(int(c) for c in num[mid:] if c != '?')
        
        left_q = num[:mid].count('?')
        right_q = num[mid:].count('?')
        
        # 1. If the total number of '?' is odd, Alice always wins
        if (left_q + right_q) % 2 != 0:
            return True
            
        # 2. Multiply by 2 on the left side to avoid division entirely
        return (left_sum - right_sum) * 2 != (right_q - left_q) * 9
