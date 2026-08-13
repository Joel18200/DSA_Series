class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:

        n = len(s)

        # tree[node] =
        # [left_char, right_char, prefix, suffix, best]
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            left_char, _, lp, ls, lb = a
            _, right_char, rp, rs, rb = b

            prefix = lp
            suffix = rs
            best = max(lb, rb)

            # Can join suffix of left with prefix of right
            if a[1] == b[0]:
                best = max(best, ls + rp)

                # Entire left segment has same character
                if lp == len_left:
                    prefix = lp + rp

                # Entire right segment has same character
                if rp == len_right:
                    suffix = rs + ls

            return [left_char, right_char, prefix, suffix, best]

        def build(node, l, r):
            if l == r:
                tree[node] = [s[l], s[l], 1, 1, 1]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = combine(
                tree[node * 2],
                tree[node * 2 + 1],
                l,
                mid,
                r
            )

        def combine(a, b, l, mid, r):
            left_char, _, lp, ls, lb = a
            _, right_char, rp, rs, rb = b

            left_len = mid - l + 1
            right_len = r - mid

            prefix = lp
            suffix = rs
            best = max(lb, rb)

            if a[1] == b[0]:
                best = max(best, ls + rp)

                if lp == left_len:
                    prefix = left_len + rp

                if rp == right_len:
                    suffix = ls + right_len

            return [left_char, right_char, prefix, suffix, best]

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = [ch, ch, 1, 1, 1]
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)

            tree[node] = combine(
                tree[node * 2],
                tree[node * 2 + 1],
                l,
                mid,
                r
            )

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1][4])

        return ans
        