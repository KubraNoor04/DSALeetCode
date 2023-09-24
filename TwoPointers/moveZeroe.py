class Solution(object):
    def moveZeroes(self, nums):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            
            if nums[slow] != 0:
                slow += 1
        return nums  # Add this line to return the modified list

solution = Solution()
nums = [1, 0, 3, 0, 2]
result = solution.moveZeroes(nums)
print(result)  # This will print the modified list
