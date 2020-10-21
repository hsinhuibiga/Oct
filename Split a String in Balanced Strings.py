#Split a String in Balanced Strings

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt=[0,0]
        ch_to_num={'L':0,'R':1}
        rst=0
        for ch in s:
            cnt[ch_to_num[ch]]+=1
            if cnt[ch_to_num[ch]]==cnt[ch_to_num[ch]-1]:
                rst+=1
                cnt[ch_to_num[ch]],cnt[ch_to_num[ch]-1]=0,0
        return rst