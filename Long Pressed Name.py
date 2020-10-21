#Long Pressed Name

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        M = len(name)
        N = len(typed)
        i, j = 0, 0
        while i < M:
            c_i = name[i]
            count_i = 0
            count_j = 0
            while i < M and name[i] == c_i:
                i += 1
                count_i += 1
            while j < N and typed[j] == c_i:
                j += 1
                count_j += 1
            if count_j < count_i:
                return False
        return True