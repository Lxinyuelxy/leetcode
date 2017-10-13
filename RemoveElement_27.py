class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        for i in range(length)[::-1]:
            if nums[i] == val:
                del nums[i]
        return len(nums)

#s = Solution()
#print(s.removeElement([1, 2, 3, 3, 4, 3], 3))
