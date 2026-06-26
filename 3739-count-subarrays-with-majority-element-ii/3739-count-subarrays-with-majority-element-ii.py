from bisect import bisect_left

class FenwickTree:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.bit):
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        prefix = [0]
        cur = 0

        # Convert target -> +1, others -> -1
        for x in nums:
            if x == target:
                cur += 1
            else:
                cur -= 1
            prefix.append(cur)

        # Coordinate Compression
        values = sorted(set(prefix))

        bit = FenwickTree(len(values))
        ans = 0

        for p in prefix:
            idx = bisect_left(values, p) + 1

            # Count previous prefix sums smaller than current
            ans += bit.query(idx - 1)

            # Insert current prefix sum
            bit.update(idx, 1)

        return ans