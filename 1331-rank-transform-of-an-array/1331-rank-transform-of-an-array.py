class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank={}
        a=[]
        for i, num in enumerate(sorted(set(arr)),1):
            rank[num]=i
        for num in arr:
            a.append(rank[num])
        return a        
            



        