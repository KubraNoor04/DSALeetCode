class Solution(object):
    def twoSum(self, nums, target):
        left, right = 0, len(nums) - 1
        
# Create a list of tuples (value, index) for each element in the nums array
        nums_index = [(nums[i], i) for i in range(len(nums))]
        nums_index.sort()

        while left < right:
            sum_twoNumbers = nums_index[left][0] + nums_index[right][0]  # Calculate the sum of the two numbers
            
            if sum_twoNumbers == target:
                return [nums_index[left][1], nums_index[right][1]]  # Return the indices of the two numbers
            elif sum_twoNumbers < target:
                left += 1
            else:
                right -= 1

        return []  