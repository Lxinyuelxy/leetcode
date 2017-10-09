class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if s[0] == '-':
            s = s[1::]
            res = int(s[::-1]) * -1
        else:
            res = int(s[::-1])
            
        if res > 0x7FFFFFFF or res < 0x80000000*-1:
            return 0
        else:
            return res
