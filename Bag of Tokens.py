#Bag of Tokens

class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        print(tokens)
        tokens.sort()
        N = len(tokens)
        left, right = 0, N - 1
        points = 0
        remain = N
        while left < N and P >= tokens[left]:
            P -= tokens[left]
            points += 1
            left += 1
            remain -= 1
        if left == 0 or left == N: return points
        while points > 0 and remain > 1:
            P += tokens[right]
            right -= 1
            points -= 1
            remain -= 1
            while left <= right and P >= tokens[left]:
                P -= tokens[left]
                points += 1
                left += 1
                remain -= 1
        return points