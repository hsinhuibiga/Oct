#Minimum Domino Rotations For Equal Row

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        N = len(A)
        count = collections.Counter(A + B)
        if count.most_common(1)[0][1] < N:
            return -1
        target = count.most_common(1)[0][0]
        a_swap = 0
        b_swap = 0
        for i in range(N):
            if A[i] == B[i]:
                if A[i] == target:
                    continue
                else:
                    return -1
            elif A[i] == target:
                b_swap += 1
            elif B[i] == target:
                a_swap += 1
            else:
                return -1
        return min(a_swap, b_swap)