class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == nums[i+1]:
                del(nums[i+1])
                length -= 1
        return length



#s = Solution()
#print(s.removeDuplicates([1,1,1,2,2,3,4,5,5]))
