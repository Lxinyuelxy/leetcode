class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return None
        else:
            res = strs[0]
            for i in range(len(strs)):
                res = self.findCommonPrefix(res, strs[i])
            return res
    
    def findCommonPrefix(self, str1, str2):
        arr_str1 = list(str1)
        arr_str2 = list(str2)
        length = len(arr_str1) if len(arr_str1)<=len(arr_str2) else len(arr_str2)
        res = ''
        for i in range(length):
            if arr_str1[i] != arr_str2[i]:
                break
            else:
                res += arr_str1[i]               
        return res

#s = Solution()
#print(s.longestCommonPrefix(['aca', 'cba']))