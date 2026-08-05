class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq={}
        for ch in range(len(nums)): 
            if nums[ch] in freq:  
                if ch-freq[nums[ch]]<=k: return True
            freq[nums[ch]]=ch   
        return False
        print(freq)         


        