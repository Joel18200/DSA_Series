class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        hashmap={}
        for a in nums1:
            for b in nums2:
                total=a+b
                if total in hashmap:
                    hashmap[total]+=1
                else:
                    hashmap[total]=1
        count=0
        for c in nums3:
            for d in nums4:
                total = c+d
                complement=-total
                if complement in hashmap:
                    count+=hashmap[complement]
        return count
        