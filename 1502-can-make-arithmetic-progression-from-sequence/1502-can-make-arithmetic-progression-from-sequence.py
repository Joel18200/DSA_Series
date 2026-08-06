class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        s=[]
        for num in range(len(arr)-1):
            i=abs(arr[num]-arr[num+1])
            s.append(i)
        return len(set(s))==1
                

            
        