class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        Z = 0
        res = ""
        count = 0
        for i,s in enumerate(S):
            if s == '(':
                count += 1
            else:
                count -= 1
            if count == 0:
                res += S[Z + 1: i]
                Z = i + 1
        return res
