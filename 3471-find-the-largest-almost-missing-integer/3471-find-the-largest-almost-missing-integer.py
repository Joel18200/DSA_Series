class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        s=Counter(nums)
        validate=[]
        #Case:1 
        '''
        When k and length of nums is same then all the elements are in a single window 
        so all have the same frequency so we will print the max value
        '''
        if len(nums)==k:
            return max(nums)
        #Case:2
        '''
        when k equals to 1 then all elements in the array is a sub-array
        so the count becomes 1 so we will return the maximum element
        if the array have duplicate elemnts then our condition is false
        so well return -1
        '''
        if k==1:
            unique_ele=[num for num in nums if s[num]==1]
            return max(unique_ele) if unique_ele else -1
        #Case:3
        '''
        In this Case the middle elements of the array always comes in atleast two sub arrays 
        so they will not satisfy the condition, so the first and last elements will be 
        available in only one sub-array which satisfies the condition,so we will take the first and last
        element and then we store they in variables so if both the elemnts has a count of 1 then
        we need to print the max element among them which is defined in return if either one of them
        has a count of 1 then that element is the printed
        '''
        num1=nums[0]
        num2=nums[-1]
        if s[num1]==1:
            validate.append(num1)
        if s[num2]==1:
            validate.append(num2)
        return max(validate) if validate else -1
        