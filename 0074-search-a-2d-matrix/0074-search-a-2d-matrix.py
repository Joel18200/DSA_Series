class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for subarray in matrix:
            left=0
            right=len(subarray)-1
            while left<=right:
                mid=left+(right-left)//2
                if subarray[mid]==target:
                    return True
                elif subarray[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
        return False                    