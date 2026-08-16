class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        # Group stones by their remainder when divided by 3
        cnt = [0] * 3
        for stone in stones:
            cnt[stone % 3] += 1
            
        # Case 1: Even number of remainder-0 stones
        if cnt[0] % 2 == 0:
            return min(cnt[1], cnt[2]) > 0
            
        # Case 2: Odd number of remainder-0 stones
        return abs(cnt[1] - cnt[2]) > 2

        