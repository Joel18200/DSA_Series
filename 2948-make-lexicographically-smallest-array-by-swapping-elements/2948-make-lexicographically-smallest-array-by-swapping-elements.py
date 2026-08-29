from typing import List
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        duplicate=nums[:]
        nums.sort()
        left,right=0,1
        current_array,groups=[],[]
        while right<len(nums):
            if nums[right] - nums[left]<= limit:
                if not current_array:
                    current_array.append(nums[left])
                current_array.append(nums[right])
                left=right
            else:
                if current_array:
                    groups.append(current_array)
                current_array=[]
                left=right
            right+=1
        if current_array:
            groups.append(current_array)
        positions = {}
        for i in range(len(duplicate)):
            if duplicate[i] not in positions:
                positions[duplicate[i]] = []
            positions[duplicate[i]].append(i)
        for group in groups:
            group_positions = []
            used = {}
            for value in group:
                if value not in used:
                    used[value] = 0
                group_positions.append(positions[value][used[value]])
                used[value] += 1
            group_positions.sort()
            group.sort()
            for i in range(len(group)):
                duplicate[group_positions[i]] = group[i]
        return duplicate


        