class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows={}
        for row,col in reservedSeats:
            if row not in rows:
                rows[row]=set()
            rows[row].add(col)

        ans=(n-len(rows))*2

        for row,seats in rows.items():
            left=all(seat not in seats for seat in range(2,6))
            right=all(seat not in seats for seat in range(6,10))
            middle=all(seat not in seats for seat in range(4,8))
            
            if left and right:
                ans+=2
            elif left or right or middle:
                ans+=1
        return ans
        

        