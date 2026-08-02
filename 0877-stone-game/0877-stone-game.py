class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(i,j):
            if i==j:
                return piles[i]
            pick_left=piles[i]-dp(i+1,j)
            pick_right=piles[j]-dp(i,j-1)
            return max(pick_left,pick_right)
        return dp(0,len(piles)-1)>=0        
        