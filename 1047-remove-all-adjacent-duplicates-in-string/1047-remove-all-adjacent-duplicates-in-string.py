class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=[]

        for i in s:
            if r and r[-1]==i:
                r.pop()
            else:
                r.append(i)
        return "".join(r)
        