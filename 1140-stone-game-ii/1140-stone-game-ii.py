class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles from i to end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        # dp[i][M] = maximum stones current player can get
        # starting from index i with M
        dp = {}

        def dfs(i, M):
            if i >= n:
                return 0

            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            if (i, M) in dp:
                return dp[(i, M)]

            best = 0

            for x in range(1, 2 * M + 1):
                # Take x piles
                # Opponent gets dfs(i+x, max(M,x))
                current = suffix[i] - dfs(i + x, max(M, x))

                best = max(best, current)

            dp[(i, M)] = best
            return best

        return dfs(0, 1)