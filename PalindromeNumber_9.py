class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        s = str(x)
        if int(s[::-1]) == x:
            return True
        else:
            return False