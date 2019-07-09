class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        Bs = len(A)
        Cs = len(A[0])
        for B in range(Bs):
            A[B] = A[B][::-1]
            for C in range(Cs):
                A[B][C]^= 1
        return A
