class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[len(nums)-1]:
            return len(nums)
        
        for i in range(1, len(nums)):
            if target == nums[i]:
                return i
            elif target>nums[i-1] and target<nums[i]:
                return i
        return 0