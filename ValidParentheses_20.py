class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack)>0 and stack.pop()=='(': pass
                else: return False
            elif s[i] == ']':
                if len(stack)>0 and stack.pop()=='[': pass
                else: return False
            elif s[i] == '}':
                if len(stack)>0 and stack.pop()=='{': pass
                else: return False

        if len(stack) > 0: return False
        return True

#s = Solution()
#print(s.isValid("(("))