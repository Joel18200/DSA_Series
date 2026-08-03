class Solution:
    def stoneGameIII(self, stoneValue):
        total_stones = len(stoneValue)

        # dp[i] = maximum score difference the current player
        # can achieve starting from index i
        score_difference = [0] * (total_stones + 1)

        for current_index in range(total_stones - 1, -1, -1):
            best_difference = float('-inf')
            current_sum = 0

            # Try taking 1, 2, or 3 stones
            for stones_taken in range(3):
                if current_index + stones_taken >= total_stones:
                    break

                current_sum += stoneValue[current_index + stones_taken]

                best_difference = max(
                    best_difference,
                    current_sum - score_difference[current_index + stones_taken + 1]
                )

            score_difference[current_index] = best_difference

        if score_difference[0] > 0:
            return "Alice"
        elif score_difference[0] < 0:
            return "Bob"
        else:
            return "Tie"
        