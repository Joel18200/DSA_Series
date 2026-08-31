class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        count_max=0
        count_min=0
        max_element=max(nums)
        min_element=min(nums)
        n=[]
        m=[]
        for i in range(len(nums)):
            if nums[i]!=max_element:
                count_max+=1
            else:
                n.append(count_max+1)
                count_max=0
        n.append(count_max+1)
        for i in range(len(nums)):
            if nums[i]!=min_element:
                count_min+=1
            else:
                m.append(count_min+1)
                count_min=0
        m.append(count_min+1)
        both_left = max(n[0], m[0])
        both_right = max(n[1], m[1])
        left_right = n[0] + m[1]
        right_left = n[1] + m[0]
        return min(both_left, both_right, left_right, right_left)
        