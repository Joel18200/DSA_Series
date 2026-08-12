class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        seen=Counter()
        left=0
        ans=0
        for right in range(len(nums)):
            seen[nums[right]]+=1
            while seen[nums[right]]>k:
                seen[nums[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans

                
