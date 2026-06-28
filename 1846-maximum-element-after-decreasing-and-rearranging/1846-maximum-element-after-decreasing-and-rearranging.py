class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n=len(arr)
        count=[0]*(n+1)
        for x in arr:
            count[min(x,n)]+=1
        ans=0    
        for value in range(1,n+1):
            while count[value]>0:
                ans=min(ans+1,value)
                count[value]-=1
        return ans        



        