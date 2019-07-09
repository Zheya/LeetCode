class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dic = {}
        for a in A: 
            if a in dic:
                return a
            else:  
                dic[a] = 1